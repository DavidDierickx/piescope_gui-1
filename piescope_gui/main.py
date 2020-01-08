import logging
import mock
import os
import threading
import time
import traceback

import click
import numpy as np
from PyQt5 import QtWidgets, QtGui, QtCore
import qimage2ndarray
import scipy.ndimage as ndi
import skimage.io
import skimage.util

import piescope

import piescope_gui.milling
import piescope_gui.correlation.main as corr
import piescope_gui.qtdesigner_files.main as gui_main
from piescope_gui.utils import display_error_message, timestamp

logger = logging.getLogger(__name__)


class GUIMainWindow(gui_main.Ui_MainGui, QtWidgets.QMainWindow):
    def __init__(self, ip_address="10.0.0.1"):
        super(GUIMainWindow, self).__init__()
        self.setupUi(self)
        self.setup_connections()
        self.microscope = None
        self.ip_address = ip_address
        self.connect_to_fibsem_microscope(ip_address=ip_address)
        # self.initialize_objective_stage()  # breaks tests, needs mocking

        self.DEFAULT_PATH = os.path.normpath(
            os.path.expanduser('~/Pictures/PIESCOPE'))
        self.setWindowTitle("PIEScope User Interface Main Window")
        self.statusbar.setSizeGripEnabled(0)
        self.status = QtWidgets.QLabel(self.statusbar)
        self.status.setAlignment(QtCore.Qt.AlignRight)
        self.statusbar.addPermanentWidget(self.status, 1)
        self.lineEdit_save_destination_FM.setText(self.DEFAULT_PATH)
        self.lineEdit_save_destination_FIBSEM.setText(self.DEFAULT_PATH)
        self.checkBox_save_destination_FM.setChecked(1)
        self.checkBox_save_destination_FIBSEM.setChecked(1)
        self.lineEdit_save_filename_FM.setText("Image")
        self.lineEdit_save_filename_FIBSEM.setText("Image")
        self.label_objective_stage_position.setText("Unknown")

        # self.liveCheck is True when ready to start live imaging,
        # and False while live imaging is running:
        self.liveCheck = True

        self.save_name = ""
        # self.laser_dict is a dictionary like: {"name": (power, exposure)}
        # with types {str: (int, int)}
        # Could refactor this out and rely only on self.lasers instead
        self.laser_dict = {}  # {"name": (power, exposure)}
        self.fibsem_image = []  # AdornedImage (for whatever is currently displayed in the FIBSEM side of the piescope GUI)
        self.array_list_FM = []  # list of 2D numpy arrays (how we open many images & use the slider for fluorescence images)
        self.display_image_fibsem = None  # AdornedImage
        self.string_list_FM = []  # list of string filenames
        self.string_list_FIBSEM = []  #TODO: REMOVE # list of string filenames
        self.current_path_FM = ""  #TODO: REMOVE
        self.current_path_FIBSEM = ""  #TODO: REMOVE
        self.current_image_FM = ""  #TODO: REMOVE. David not sure why these are strings.
        self.current_image_FIBSEM = ""  #TODO: REMOVE. David not sure why these are strings.
        self.current_pixmap_FM = []  #TODO: should be None, not an empty list to start with. PixMap object (pyqt)
        self.current_pixmap_FIBSEM = []  #TODO: should be None, not an empty list to start with. PixMap object (pyqt)
        self.save_destination_FM = self.DEFAULT_PATH
        self.save_destination_FIBSEM = self.DEFAULT_PATH
        self.save_destination_correlation = self.DEFAULT_PATH

    def setup_connections(self):

        self.lasers = piescope.lm.laser.initialize_lasers()
        self.detector = piescope.lm.detector.Basler()

        self.comboBox_resolution.currentTextChanged.connect(
            lambda: self.update_fibsem_settings())
        self.lineEdit_dwell_time.textChanged.connect(
            lambda: self.update_fibsem_settings())

        self.actionOpen_FM_Image.triggered.connect(
            lambda: self.open_images("FM"))
        self.actionOpen_FIBSEM_Image.triggered.connect(
            lambda: self.open_images("FIBSEM"))

        self.actionSave_FM_Image.triggered.connect(
            lambda: self.save_image("FM"))
        self.actionSave_FIBSEM_Image.triggered.connect(
            lambda: self.save_image("FIBSEM"))

        self.slider_stack_FM.valueChanged.connect(
            lambda: self.update_display("FM"))
        self.slider_stack_FIBSEM.valueChanged.connect(
            lambda: self.update_display("FIBSEM"))

        self.button_save_destination_FM.clicked.connect(
            lambda: self.fill_destination("FM"))
        self.button_save_destination_FIBSEM.clicked.connect(
            lambda: self.fill_destination("FIBSEM"))
        self.toolButton_correlation_output.clicked.connect(
            self.fill_correlation_destination)

        self.checkBox_laser1.clicked.connect(
            lambda: self.update_laser_dict("laser640"))
        self.checkBox_laser2.clicked.connect(
            lambda: self.update_laser_dict("laser561"))
        self.checkBox_laser3.clicked.connect(
            lambda: self.update_laser_dict("laser488"))
        self.checkBox_laser4.clicked.connect(
            lambda: self.update_laser_dict("laser405"))

        self.slider_laser1.valueChanged.connect(
            lambda: self.update_laser_dict("laser640"))
        self.slider_laser2.valueChanged.connect(
            lambda: self.update_laser_dict("laser561"))
        self.slider_laser3.valueChanged.connect(
            lambda: self.update_laser_dict("laser488"))
        self.slider_laser4.valueChanged.connect(
            lambda: self.update_laser_dict("laser405"))

        self.lineEdit_exposure_1.textChanged.connect(
            lambda: self.update_laser_dict("laser640"))
        self.lineEdit_exposure_2.textChanged.connect(
            lambda: self.update_laser_dict("laser561"))
        self.lineEdit_exposure_3.textChanged.connect(
            lambda: self.update_laser_dict("laser488"))
        self.lineEdit_exposure_4.textChanged.connect(
            lambda: self.update_laser_dict("laser405"))

        self.button_get_image_FIB.clicked.connect(
            lambda: self.get_FIB_image())
        self.button_get_image_SEM.clicked.connect(
            lambda: self.get_SEM_image())
        self.button_last_image_FIB.clicked.connect(
            lambda: self.get_last_FIB_image())
        self.button_last_image_SEM.clicked.connect(
            lambda: self.get_last_SEM_image())

        self.button_get_image_FM.clicked.connect(
            lambda: self.fluorescence_image(
                self.comboBox_laser_basler.currentText(),
                self.lineEdit_exposure_basler.text(),
                self.lineEdit_power_basler_2.text()))
        self.button_live_image_FM.clicked.connect(
            lambda: self.fluorescence_live_imaging(
                self.comboBox_laser_basler.currentText(),
                self.lineEdit_exposure_basler.text(),
                self.lineEdit_power_basler_2.text()))

        self.pushButton_initialize_stage.clicked.connect(
            lambda: self.initialize_objective_stage())
        self.pushButton_move_absolute.clicked.connect(
            lambda: self.move_absolute_objective_stage(
                self.lineEdit_move_absolute.text()))
        self.pushButton_move_relative.clicked.connect(
            lambda: self.move_relative_objective_stage())

        self.connect_microscope.clicked.connect(
            lambda: self.connect_to_fibsem_microscope(self.ip_address))
        self.to_light_microscope.clicked.connect(
            lambda: self.move_to_light_microscope())
        self.to_electron_microscope.clicked.connect(
            lambda: self.move_to_electron_microscope())

        self.pushButton_volume.clicked.connect(self.acquire_volume)
        self.pushButton_correlation.clicked.connect(self.correlateim)
        self.pushButton_milling.clicked.connect(self.milling)

        self.pushButton_save_objective_position.clicked.connect(
            self.save_objective_stage_position)
        self.pushButton_go_to_saved_position.clicked.connect(
            self.move_to_saved_objective_position)
        self.pushButton_get_position.clicked.connect(
            self.get_objective_stage_position)

    ############## FIBSEM microscope methods ##############
    def connect_to_fibsem_microscope(self, ip_address="10.0.0.1"):
        """Connect to the FIBSEM microscope."""
        try:
            from piescope import fibsem
            self.microscope = piescope.fibsem.initialize(ip_address=ip_address)
            self.camera_settings = self.update_fibsem_settings()
        except Exception as e:
            display_error_message(traceback.format_exc())
        else:
            print("Success: connected to the FIBSEM microscope "
                  "(using ip address: {})".format(ip_address)
                  )

    def update_fibsem_settings(self):
        if not self.microscope:
            self.connect_to_fibsem_microscope()
        try:
            from piescope import fibsem
            dwell_time = float(self.lineEdit_dwell_time.text())*1.e-6
            resolution = self.comboBox_resolution.currentText()
            fibsem_settings = piescope.fibsem.update_camera_settings(dwell_time, resolution)
            self.camera_settings = fibsem_settings
            return fibsem_settings
        except Exception as e:
            display_error_message(traceback.format_exc())

    ############## FIBSEM sample stage methods ##############
    def move_to_light_microscope(self, x=+49.952e-3, y=-0.1911e-3):
        try:
            piescope.fibsem.move_to_light_microscope(self.microscope, x, y)
        except Exception as e:
            display_error_message(traceback.format_exc())
        else:
            print("Moved to light microscope.")

    def move_to_electron_microscope(self, x=-49.952e-3, y=+0.1911e-3):
        try:
            piescope.fibsem.move_to_electron_microscope(self.microscope, x, y)
        except Exception as e:
            display_error_message(traceback.format_exc())
        else:
            print("Moved to electron microscope.")

    ############## FIBSEM image methods ##############
    def get_FIB_image(self):
        try:
            if self.checkBox_Autocontrast.isChecked():
                self.autocontrast_ion_beam()
            self.image_ion = piescope.fibsem.new_ion_image(self.microscope, self.camera_settings)
            self.display_image_fibsem = np.copy(self.image_ion.data)
            self.update_display("FIBSEM")
        except Exception as e:
            display_error_message(traceback.format_exc())
        else:
            return self.image_ion

    def get_last_FIB_image(self):
        try:
            self.image_ion = piescope.fibsem.last_ion_image(self.microscope)
            self.display_image_fibsem = skimage.util.img_as_ubyte(self.image_ion.data)
            self.update_display("FIBSEM")
        except Exception as e:
            display_error_message(traceback.format_exc())
        else:
            return self.image_ion

    def get_SEM_image(self):
        try:
            self.image_sem = piescope.fibsem.new_electron_image(self.microscope, self.camera_settings)
            self.display_image_fibsem = np.copy(self.image_sem.data)
            self.display_image_fibsem = ndi.median_filter(self.display_image_fibsem, 2)
            self.update_display("FIBSEM")
        except Exception as e:
            display_error_message(traceback.format_exc())
        else:
            return self.image_sem

    def get_last_SEM_image(self):
        try:
            self.fibsem_image = piescope.fibsem.last_electron_image(self.microscope)
            self.display_image_fibsem = self.fibsem_image.data
            self.display_image_fibsem = skimage.util.img_as_ubyte(self.display_image_fibsem)
            self.update_display("FIBSEM")
        except Exception as e:
            display_error_message(traceback.format_exc())
        else:
            return self.fibsem_image

    def autocontrast_ion_beam(self):
        try:
            self.microscope.imaging.set_active_view(2)  # the ion beam view
            print("Running ion beam autocontrast")
            piescope.fibsem.autocontrast(self.microscope)
            self.fibsem_image = piescope.fibsem.last_ion_image(self.microscope)
            self.display_image_fibsem = skimage.util.img_as_ubyte(self.fibsem_image.data)
            self.update_display("FIBSEM")
        except Exception as e:
            display_error_message(traceback.format_exc())
        else:
            return self.fibsem_image

    ############## Fluorescence detector methods ##############
    def fluorescence_image(self, wavelength, exposure_time, laser_power):
        """Acquire a new fluorescence image.

        Parameters
        ----------
        wavelength : str
            Wavelength of laser to use for fluorescence imaging.
            Available values: '640nm', '561nm', '488nm', or '405nm'.
        exposure_time : float
            Exposure time, in milliseconds (ms).
        laser_power : float
            Laser power to use in live imaging.

        Returns
        -------
        numpy ndarray
            The fluorescence image acquired. Format is as a uint8 numpy array.
        """
        try:
            from pypylon import genicam
            # Setup
            exposure_in_microseconds = float(exposure_time) * 1000  # convert
            WAVELENGTH_TO_LASERNAME = {"640nm": "laser640",
                                       "561nm": "laser561",
                                       "488nm": "laser488",
                                       "405nm": "laser405"}
            laser_name = WAVELENGTH_TO_LASERNAME[wavelength]
            self.lasers[laser_name].laser_power = float(laser_power)
            # Acquire image
            self.lasers[laser_name].emission_on()
            try:
                image = self.detector.camera_grab(exposure_in_microseconds)
            except genicam.RuntimeException:
                display_error_message(
                    "Please turn off the live imaging "
                    "before acquiring a new fluorescence image.")
                return
            finally:
                self.lasers[laser_name].emission_off()
            # Update GUI
            self.string_list_FM = [self.DEFAULT_PATH + os.path.sep + "F_" + timestamp()]
            self.array_list_FM = image
            self.slider_stack_FM.setValue(1)
            self.update_display("FM")
        except Exception as e:
            display_error_message(traceback.format_exc())
        else:
            print("Fluorescence image acquired.")
            return image

    def live_imaging_worker(self, stop_event, laser_name, laser_power,
                            exposure_time, image_frame_interval=None):
        """Worker function for live imaging thread.

        Parameters
        ----------
        stop_event : threading.Event()
            Signal to terminate the thread.
        laser_name : str
            Name of laser to use in live imaging.
            Available values are "laser640", "laser561", "laser488", "laser405"
        laser_power : float
            Laser power to use in live imaging.
        exposure_time : float
            Exposure time, in milliseconds (ms).
        image_frame_interval : float, optional
            Waiting period between acquisition of live imaging frames.
            By default, None. This means live images will be acquired as fast
            as possible. Note the laser stays on even if imaging is paused.
        """
        # Setup
        print("Live imaging mode running...")
        self.liveCheck = False
        self.button_live_image_FM.setDown(True)
        self.lasers[laser_name].laser_power = float(laser_power)
        self.lasers[laser_name].emission_on()
        exposure_in_microseconds = float(exposure_time) * 1000  # conversion
        # Running live imaging
        while not stop_event.isSet():
            image = self.detector.camera_grab(exposure_in_microseconds)
            # Update GUI
            self.string_list_FM = [self.DEFAULT_PATH + os.path.sep + "F_" + timestamp()]
            self.array_list_FM = image
            self.slider_stack_FM.setValue(1)
            self.update_display("FM")
            # Pause between frames if desired (the laser will remain on)
            if image_frame_interval is not None:
                stopevent.wait(image_frame_interval)
        # Teardown / cleanup
        print("Stopping live imaging mode.")
        self.lasers[laser_name].emission_off()
        self.detector.camera.Close()
        self.liveCheck = True
        self.button_live_image_FM.setDown(False)

    def fluorescence_live_imaging(self, wavelength, exposure_time, laser_power,
                                  image_frame_interval=None):
        """Fluorescence live imaging.

        Parameters
        ----------
        wavelength : str
            Which laser wavelength to use for live imaging.
            Available values are: "640nm", "561nm", "488nm", or "405nm".
        exposure_time : float
            Exposure time, in milliseconds.
        laser_power : float
            Laser power to use for live imaging.
        image_frame_interval : float, optional
            Waiting period between acquisition of live imaging frames.
            By default, None. This means live images will be acquired as fast
            as possible. Note the laser stays on even if imaging is paused.
        """
        try:
            WAVELENGTH_TO_LASERNAME = {"640nm": "laser640",
                                        "561nm": "laser561",
                                        "488nm": "laser488",
                                        "405nm": "laser405"}
            laser_name = WAVELENGTH_TO_LASERNAME[wavelength]
            if self.liveCheck is True:
                self.stop_event = threading.Event()
                self._thread = threading.Thread(
                    target=self.live_imaging_worker,
                    args=(self.stop_event,
                          laser_name,
                          laser_power,
                          exposure_time,
                          image_frame_interval))
                self._thread.start()
            else:
                self.stop_event.set()
        except (KeyboardInterrupt, SystemExit):
            self.stop_event.set()
        except Exception as e:
            display_error_message(traceback.format_exc())

    ############## Fluorescence objective lens stage methods ##############
    def initialize_objective_stage(self, time_delay=0.3, testing=False):
        """Initialize the fluorescence objective lens stage.

        Parameters
        ----------
        time_delay : float, optional
            Pause in seconds, after initializing objective lens stage settings.
        testing : bool, optional
            For use in tests with hardware offline, by default False.

        Returns
        -------
        StageController
            Objective stage object for fluorescence imaging.
        """
        try:
            stage = piescope.lm.objective.StageController(testing=testing)
            stage.initialise_system_parameters()
            self.objective_stage = stage
            time.sleep(time_delay)
            self.get_objective_stage_position()
        except Exception as e:
            display_error_message(traceback.format_exc())
        else:
            print("Success: objective lens stage initialised")
            return stage

    def get_objective_stage_position(self):
        """Get the current objective stage position.

        Returns
        -------
        float
            Objective stage position in microns (um).
        """
        try:
            pos = self.objective_stage.current_position()
            pos = float(pos) / 1000  # convert from nanometers to microns
        except Exception as e:
            display_error_message(traceback.format_exc())
        else:
            self.label_objective_stage_position.setText(str(pos))
            return pos

    def save_objective_stage_position(self):
        """Save the current objecitve stage position.

        Returns
        -------
        float
            Objective stage position in microns (um).
        """
        try:
            pos = self.get_objective_stage_position()
            self.label_objective_stage_saved_position.setText(str(pos))
        except Exception as e:
            display_error_message(traceback.format_exc())
        else:
            return pos

    def move_to_saved_objective_position(self):
        """Move objective lens stage to the saved position.

        Returns
        -------
        float
            New position of objective lens stage, in microns (um).
        """
        pos = self.label_objective_stage_saved_position.text()
        if pos == '':
            display_error_message(
                "There is no saved objective stage position.")
            return
        else:
            new_position = self.move_absolute_objective_stage(position=pos)
            return new_position

    def move_absolute_objective_stage(self, position='', time_delay=0.3):
        """Absolute movement of the fluorescence objective lens stage.

        Parameters
        ----------
        position : str, optional
            Absolute position to move to, in microns (um), by default ''.
            If empty string is given, we read the value from the GUI.
        time_delay : float, optional
            Pause in seconds, after moving the objective lens stage.

        Returns
        -------
        float
            New position of objective lens stage, in microns (um).
        """
        if position == '':
            position = self.label_objective_stage_saved_position.text()
            if position == '':
                display_error_message(
                    "Please provide user input to 'Move absolute' for the "
                    "objective stage (an empty string was received).")
                return
        try:
            position = int(float(position)*1000)  # convert to nanometers
        except ValueError:
            display_error_message(
                "Please provide a number as user input to 'Move absolute' "
                "for the objective stage (the string could not be converted).")
            return
        try:
            logger.debug("Absolute move the objective stage to position at "
                         "{} nanometers.".format(position))
            answer = self.objective_stage.move_absolute(position)
            time.sleep(time_delay)
            new_position = self.get_objective_stage_position()
            logger.debug("After absolute move, objective stage is now at "
                         "position: {} nanometers.".format(new_position))
        except Exception:
            display_error_message(traceback.format_exc())
        else:
            return new_position

    def move_relative_objective_stage(self, distance='', time_delay=0.3):
        """Relative movement of the fluorescence objective lens stage.

        Parameters
        ----------
        distance : str, optional
            Relative distance to move in microns (um), by default ''.
            If an empty string is given, we read the value from the GUI.
        time_delay : float, optional
            Pause in seconds, after moving the objective lens stage.

        Returns
        -------
        float
            New position of objective lens stage, in microns (um).
        """
        if distance == '':
            distance = self.lineEdit_move_relative.text()
            if distance == '':
                display_error_message(
                    "Please provide user input to 'Move relative' for the "
                    "objective stage (an empty string was received).")
                return
        try:
            distance = int(float(distance) * 1000)  # convert to nanometers
        except ValueError:
            display_error_message(
                "Please provide a number as user input to 'Move relative' "
                "for the objective stage (the string could not be converted).")
            return
        try:
            logger.debug("Relative move the objective stage by "
                         "{} nanometers.".format(distance))
            answer = self.objective_stage.move_relative(distance)
            time.sleep(time_delay)
            new_position = self.get_objective_stage_position()
            logger.debug("After relative move, objective stage is now at "
                         "position: {} nanometers.".format(new_position))
        except Exception:
            display_error_message(traceback.format_exc())
        else:
            return new_position

    ############## Fluorescence laser methods ##############
    def update_laser_dict(self, laser):
        logger.debug("Updating laser dictionary")
        logger.debug("{}".format(laser))
        logger.debug(self.lasers)
        logger.debug(self.lasers[laser])
        try:
            assert laser == self.lasers[laser].NAME
            if laser == "laser640":
                laser_selected = self.checkBox_laser1.isChecked()
                laser_power = int(self.spinBox_laser1.text())
                exposure_time = int(self.lineEdit_exposure_1.text())
                widget_spinbox = self.spinBox_laser1
                widget_slider = self.slider_laser1
                widget_textexposure = self.lineEdit_exposure_1
            elif laser == "laser561":
                laser_selected = self.checkBox_laser2.isChecked()
                laser_power = int(self.spinBox_laser2.text())
                exposure_time = int(self.lineEdit_exposure_2.text())
                widget_spinbox = self.spinBox_laser2
                widget_slider = self.slider_laser2
                widget_textexposure = self.lineEdit_exposure_2
            elif laser == "laser488":
                laser_selected = self.checkBox_laser3.isChecked()
                laser_power = int(self.spinBox_laser3.text())
                exposure_time = int(self.lineEdit_exposure_3.text())
                widget_spinbox = self.spinBox_laser3
                widget_slider = self.slider_laser3
                widget_textexposure = self.lineEdit_exposure_3
            elif laser == "laser405":
                laser_selected = self.checkBox_laser4.isChecked()
                laser_power = int(self.spinBox_laser4.text())
                exposure_time = int(self.lineEdit_exposure_4.text())
                widget_spinbox = self.spinBox_laser4
                widget_slider = self.slider_laser4
                widget_textexposure = self.lineEdit_exposure_4
            # Update laser object attributes
            self.lasers[laser].selected = laser_selected
            self.lasers[laser].laser_power = laser_power
            self.lasers[laser].exposure_time = exposure_time
            laser_dict = {}
            for i in self.lasers.values():
                if i.selected is True:
                    laser_dict[i.NAME] = (i.laser_power, i.exposure_time)
            self.laser_dict = laser_dict
            # Grey out laser contol widgets if laser checkbox is not selected
            if laser_selected:
                widget_slider.setEnabled(1)
                widget_textexposure.setEnabled(1)
                widget_spinbox.setEnabled(1)
            else:
                widget_slider.setEnabled(0)
                widget_textexposure.setEnabled(0)
                widget_spinbox.setEnabled(0)
        except Exception as e:
            display_error_message(traceback.format_exc())

    ############## Image methods ##############
    def open_images(self, modality):
        """Open image files and display the first"""
        try:
            if modality == "FM":
                [self.string_list_FM,
                 ext] = QtWidgets.QFileDialog.getOpenFileNames(
                    self, 'Open File',
                    filter="Images (*.bmp *.tif *.tiff *.jpg)")

                if self.string_list_FM:
                    self.array_list_FM = _create_array_list(
                        self.string_list_FM, "FM")
                    self.slider_stack_FM.setMaximum(len(self.string_list_FM))
                    self.spinbox_slider_FM.setMaximum(len(self.string_list_FM))
                    self.slider_stack_FM.setValue(1)
                    self.update_display("FM")

            elif modality == "FIBSEM":
                [self.string_list_FIBSEM,
                 ext] = QtWidgets.QFileDialog.getOpenFileNames(
                    self, 'Open File',
                    filter="Images (*.bmp *.tif *.tiff *.jpg)")

                if self.string_list_FIBSEM:
                    self.display_image_fibsem = _create_array_list(
                        self.string_list_FIBSEM, "FIBSEM")
                    self.slider_stack_FIBSEM.setMaximum(
                        len(self.string_list_FIBSEM))
                    self.spinbox_slider_FIBSEM.setMaximum(
                        len(self.string_list_FIBSEM))
                    self.slider_stack_FIBSEM.setValue(1)
                    self.update_display("FIBSEM")
        except Exception as e:
            display_error_message(traceback.format_exc())

    def save_image(self, modality):
        """Save image on display """
        try:
            if modality == "FM":
                if self.current_image_FM is not None:
                    max_value = len(self.string_list_FM)
                    if max_value == 1:
                        display_image = self.array_list_FM
                        print(display_image)
                    else:
                        display_image = self.array_list_FM[
                            self.slider_stack_FM.value() - 1]
                        print(display_image)
                    [save_base, ext] = os.path.splitext(
                        self.lineEdit_save_filename_FM.text())
                    dest = self.lineEdit_save_destination_FM.text() + \
                        os.path.sep + save_base + ".tif"
                    print(self.lineEdit_save_destination_FM.text())
                    print(os.path.sep)
                    print(save_base)
                    print(dest)
                    dir_exists = os.path.isdir(
                        self.lineEdit_save_destination_FM.text())
                    if not dir_exists:
                        os.makedirs(self.lineEdit_save_destination_FM.text())
                        piescope.utils.save_image(display_image, dest)
                    else:
                        exists = os.path.isfile(dest)
                        if not exists:
                            piescope.utils.save_image(display_image, dest)
                        else:
                            count = 1
                            while exists:
                                dest = (self.lineEdit_save_destination_FM.text()
                                        + os.path.sep + save_base + "("
                                        + str(count) + ").tif")
                                exists = os.path.isfile(dest)
                                count = count + 1
                                piescope.utils.save_image(display_image, dest)
                else:
                    display_error_message("No image to save")

            elif modality == "FIBSEM":
                if self.current_image_FIBSEM is not None:
                    display_image = self.fibsem_image
                    [save_base, ext] = os.path.splitext(
                        self.lineEdit_save_filename_FIBSEM.text())
                    dest = self.lineEdit_save_destination_FIBSEM.text() + \
                           os.path.sep + save_base + ".tif"
                    print(self.lineEdit_save_destination_FIBSEM.text())
                    print(os.path.sep)
                    print(self.lineEdit_save_filename_FIBSEM.text())
                    print(save_base)
                    print(ext)
                    print(dest)
                    dir_exists = os.path.isdir(
                        self.lineEdit_save_destination_FIBSEM.text())
                    if not dir_exists:
                        os.makedirs(
                            self.lineEdit_save_destination_FIBSEM.text())
                        piescope.utils.save_image(display_image, dest)
                    else:
                        exists = os.path.isfile(dest)
                        if not exists:
                            piescope.utils.save_image(display_image, dest)
                        else:
                            count = 1
                            while exists:
                                dest = (self.lineEdit_save_destination_FIBSEM.text()
                                        + os.path.sep + save_base + "("
                                        + str(count) + ").tif")
                                exists = os.path.isfile(dest)
                                count = count + 1
                                piescope.utils.save_image(display_image, dest)

                else:
                    display_error_message("No image to save")

        except Exception as e:
            display_error_message(traceback.format_exc())

    def update_display(self, modality):
        """Update the GUI display with the current image"""
        try:
            if modality == "FM" and self.string_list_FM:
                # Updating display of GUI with current FM display image
                slider_value = str(self.slider_stack_FM.value())
                max_value = str(len(self.string_list_FM))

                image_string = self.string_list_FM[int(slider_value) - 1]
                self.current_path_FM = os.path.normpath(image_string)

                if int(max_value) > 1:
                    image_array = self.array_list_FM[int(slider_value) - 1]
                else:
                    image_array = self.array_list_FM
                image_array = np.flipud(image_array)
                FM_max = image_array.max()
                self.label_max_FM_value.setText("Max value: " + str(FM_max))
                image_array_crosshair = np.copy(image_array)
                xshape = image_array_crosshair.shape[0]
                yshape = image_array_crosshair.shape[1]
                midx = int(xshape/2)
                midy = int(yshape/2)
                thresh = 2
                mult = 25
                image_array_crosshair[midx-(thresh*mult):midx+(thresh*mult), midy-thresh:midy+thresh] = 255
                image_array_crosshair[midx - thresh:midx + thresh, midy - (thresh * mult):midy + (thresh * mult)] = 255

                self.current_image_FM = qimage2ndarray.array2qimage(image_array.copy())
                self.current_image_FM_crosshair = qimage2ndarray.array2qimage(image_array_crosshair.copy())
                self.status.setText("Image " + slider_value + " of " + max_value)

                self.current_pixmap_FM = QtGui.QPixmap.fromImage(
                    self.current_image_FM_crosshair)
                self.current_pixmap_FM = self.current_pixmap_FM.scaled(
                    640, 400, QtCore.Qt.KeepAspectRatio)
                self.label_image_FM.setPixmap(self.current_pixmap_FM)

            elif modality == "FIBSEM" and self.display_image_fibsem is not None:
                # Updating display of GUI with current FIBSEM display image
                self.qimagearray_fibsem = qimage2ndarray.array2qimage(np.copy(self.display_image_fibsem))
                self.current_pixmap_fibsem = QtGui.QPixmap.fromImage(
                    self.qimagearray_fibsem)
                self.current_pixmap_fibsem = self.current_pixmap_fibsem.scaled(
                    640, 400, QtCore.Qt.KeepAspectRatio)
                self.label_image_FIBSEM.setPixmap(self.current_pixmap_fibsem)

        except Exception as e:
            display_error_message(traceback.format_exc())

    def fill_destination(self, modality):
        """Fills the destination box with the text from the directory"""
        try:
            if modality == "FM":
                if not self.checkBox_save_destination_FM.isChecked():
                    self.save_destination_FM = os.path.normpath(
                        QtWidgets.QFileDialog.getExistingDirectory(
                            self, 'File Destination'))
                    destination_text = self.save_destination_FM + os.path.sep
                    self.lineEdit_save_destination_FM.setText(destination_text)
                    return destination_text
            elif modality == "FIBSEM":
                if not self.checkBox_save_destination_FIBSEM.isChecked():
                    self.save_destination_FIBSEM = os.path.normpath(
                        QtWidgets.QFileDialog.getExistingDirectory(
                            self, 'File Destination'))
                    destination_text = \
                        self.save_destination_FIBSEM + os.path.sep
                    self.lineEdit_save_destination_FIBSEM.setText(
                        destination_text)
                    return destination_text
        except Exception as e:
            display_error_message(traceback.format_exc())

    def fill_correlation_destination(self):
        self.save_destination_correlation = os.path.normpath(
            QtWidgets.QFileDialog.getExistingDirectory(
                self, 'File Destination'))
        destination_text = self.save_destination_correlation + os.path.sep
        self.correlation_output_path.setText(destination_text)
        return destination_text

    def acquire_volume(self):
        try:
            laser_dict = self.laser_dict
            if laser_dict == {}:
                raise ValueError("No lasers selected")
            if len(laser_dict) > 3:
                raise ValueError("Select max 3 lasers")

            num_z_slices = int(self.lineEdit_slice_number.text())
            if num_z_slices < 0:
                raise ValueError("Number of slices must be a positive integer")

            z_slice_distance = int(self.lineEdit_slice_distance.text())
            if z_slice_distance < 0:
                raise ValueError("Slice distance must be a positive integer")

            timestamp_string = timestamp()
            volume = piescope.lm.volume.volume_acquisition(
                laser_dict, num_z_slices, z_slice_distance)

            output_directory = self.lineEdit_save_destination_FM.text()
            fname_include = self.lineEdit_save_filename_FM.text()
            fname_volume = 'Volume_' + fname_include + '_' + timestamp_string + '.tif'
            filename_volume = os.path.join(output_directory, fname_volume)
            piescope.utils.save_image(image=volume, destination=filename_volume)

            # Maximum intensity projection
            max_intensity = piescope.utils.max_intensity_projection(volume)
            fname_max_intensity = 'MIP_' + fname_include + '_' + timestamp_string + '.tif'
            filename_max_intensity = os.path.join(output_directory, fname_max_intensity)
            piescope.utils.save_image(image=max_intensity, destination=filename_max_intensity)

            # Display an RGB maximum intensity projection of volume image
            max_intensity_rgb = piescope.utils.rgb_image(max_intensity)
            self.string_list_FM = ["RGB image"]
            self.array_list_FM = max_intensity_rgb
            self.update_display("FM")

        except Exception as e:
            display_error_message(traceback.format_exc())

    def correlateim(self):
        tempfile = "C:"
        try:
            fluorescence_image = self.array_list_FM
            print(type(fluorescence_image))

            if fluorescence_image == [] or fluorescence_image == "":
                raise ValueError("No first image selected")
            fibsem_image = self.display_image_fibsem
            if fibsem_image == [] or fibsem_image == "":
                raise ValueError("No second image selected")

            output_filename = self.correlation_output_path.text()
            if output_filename == "":
                raise ValueError("No path selected")
            if not os.path.isdir(output_filename):
                raise ValueError("Please select a valid directory")

            image_ext = "\\correlated_image_" + timestamp()
            copy_count = 1

            while os.path.isfile(output_filename + image_ext + "_" + str(copy_count) + ".tiff"):
                copy_count = copy_count + 1

            tempfile = output_filename + image_ext + "_" + str(copy_count) + "temp_.tiff"
            open(tempfile, "w+")

            output_filename = output_filename + image_ext + "_" + str(copy_count) + ".tiff"

            window = corr.open_correlation_window(
                self, fluorescence_image, fibsem_image, output_filename)
            window.showMaximized()
            window.show()

            window.exitButton.clicked.connect(lambda: self.mill_window_from_correlation(window))

            if os.path.isfile(tempfile):
                os.remove(tempfile)

        except Exception as e:
            if os.path.isfile(tempfile):
                os.remove(tempfile)
            display_error_message(traceback.format_exc())

    def mill_window_from_correlation(self, window):
        aligned_image = window.menu_quit()
        piescope_gui.milling.open_milling_window(self, aligned_image)#, overlay_adorned_image, fluorescence_image_rgb, fluorescence_original, output, matched_points_dict)

    def milling(self):
        try:
            filename, _ = QtWidgets.QFileDialog.getOpenFileName(
                self, 'Open Milling Image',
                filter="Images (*.bmp *.tif *.tiff *.jpg)"
                )

            from autoscript_sdb_microscope_client.structures import AdornedImage
            adorned_image = AdornedImage()
            adorned_image = adorned_image.load(filename)
            if filename:
                image = _create_array_list(filename, "MILLING")
            else:
                raise ValueError("No image selected")

            piescope_gui.milling.open_milling_window(self, image, adorned_image)

        except Exception as e:
            display_error_message(traceback.format_exc())


def _create_array_list(input_list, modality):
    if modality == "FM":
        if len(input_list) > 1:
            array_list_FM = skimage.io.imread_collection(input_list, conserve_memory=True)
        else:
            array_list_FM = skimage.io.imread(input_list[0])
            print("ARRAY LIST IS:", array_list_FM)
        return array_list_FM
    elif modality == "FIBSEM":
        if len(input_list) > 1:
            array_list_FIBSEM = skimage.io.imread_collection(input_list)
        else:
            array_list_FIBSEM = skimage.io.imread(input_list[0])
        return array_list_FIBSEM
    elif modality == "MILLING":
        if len(input_list) > 1:
            array_list_MILLING = skimage.io.imread_collection(input_list)
        else:
            array_list_MILLING = skimage.io.imread(input_list[0])
        return array_list_MILLING


@click.command()
@click.option('--offline', default='False')
def main(offline):
    """Start the main `piescope_gui` graphical user interface.

    To launch `piescope_gui` when connected to all the microscope hardware:
    ```
    piescope
    ```
    or...
    ```
    python piescope_gui/main.py
    ```

    To launch `piescope_gui` in offline mode for testing
    (you will need an offline scripting version of AutoScript installed),
    call `piescope_gui` using the `--offline=True` command line option:
    ```
    piescope --offline=True
    ```
    or...
    ```
    python piescope_gui/main.py --offline=True
    ```

    Parameters
    ----------
    offline : bool
        Default value is False, which launches the `piescope_gui` & assumes
        it's connected correctly to all the microscope hardware.
        If offline is True, we launch `piescope_gui` using:
        * The Basler offline emulator for the fluorescence detector.
        * A mock patch for the SMARACT objective lens stage.
        * AutoScript via "localhost" (requires offline scripting installation).
    """
    if offline.lower() == 'false':
        logging.basicConfig(level=logging.WARNING)
        launch_gui(ip_address='10.0.0.1')
    elif offline.lower() == 'true':
        logging.basicConfig(level=logging.DEBUG)
        with mock.patch.dict('os.environ', {'PYLON_CAMEMU': '1'}):
            with mock.patch('piescope.lm.objective.StageController',
                            autospec=True) as mock_objective:
                instance = mock_objective.return_value
                instance.current_position.return_value = 0

                try:
                    launch_gui(ip_address="localhost")
                except Exception:
                    import pdb
                    traceback.print_exc()
                    pdb.set_trace()


def launch_gui(ip_address='10.0.0.1'):
    """Launch the `piescope_gui` main application window."""
    app = QtWidgets.QApplication([])
    qt_app = GUIMainWindow(ip_address=ip_address)
    qt_app.show()
    app.exec_()


if __name__ == '__main__':
    main()
