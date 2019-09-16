# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainGui(object):
    def setupUi(self, MainGui):
        MainGui.setObjectName("MainGui")
        MainGui.resize(852, 734)
        MainGui.setMinimumSize(QtCore.QSize(572, 734))
        self.centralwidget = QtWidgets.QWidget(MainGui)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.frame_main = QtWidgets.QFrame(self.centralwidget)
        self.frame_main.setMinimumSize(QtCore.QSize(554, 675))
        self.frame_main.setMaximumSize(QtCore.QSize(554, 675))
        self.frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_main)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_slider = QtWidgets.QFrame(self.frame_main)
        self.frame_slider.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_slider.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_slider.setObjectName("frame_slider")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_slider)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.layout_image_vertical = QtWidgets.QVBoxLayout()
        self.layout_image_vertical.setObjectName("layout_image_vertical")
        self.layout_image_horizontal = QtWidgets.QHBoxLayout()
        self.layout_image_horizontal.setObjectName("layout_image_horizontal")
        self.label_slider = QtWidgets.QLabel(self.frame_slider)
        self.label_slider.setObjectName("label_slider")
        self.layout_image_horizontal.addWidget(self.label_slider)
        spacerItem = QtWidgets.QSpacerItem(668, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_image_horizontal.addItem(spacerItem)
        self.spinbox_slider = QtWidgets.QSpinBox(self.frame_slider)
        self.spinbox_slider.setMinimumSize(QtCore.QSize(37, 20))
        self.spinbox_slider.setMaximumSize(QtCore.QSize(37, 20))
        self.spinbox_slider.setMinimum(1)
        self.spinbox_slider.setMaximum(1)
        self.spinbox_slider.setProperty("value", 1)
        self.spinbox_slider.setObjectName("spinbox_slider")
        self.layout_image_horizontal.addWidget(self.spinbox_slider)
        self.layout_image_vertical.addLayout(self.layout_image_horizontal)
        self.slider_stack = QtWidgets.QSlider(self.frame_slider)
        self.slider_stack.setMinimum(1)
        self.slider_stack.setMaximum(1)
        self.slider_stack.setSingleStep(1)
        self.slider_stack.setProperty("value", 1)
        self.slider_stack.setOrientation(QtCore.Qt.Horizontal)
        self.slider_stack.setObjectName("slider_stack")
        self.layout_image_vertical.addWidget(self.slider_stack)
        self.gridLayout_2.addLayout(self.layout_image_vertical, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_slider, 3, 1, 1, 1)
        self.frame_save_destination = QtWidgets.QFrame(self.frame_main)
        self.frame_save_destination.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_save_destination.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_save_destination.setObjectName("frame_save_destination")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_save_destination)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_save_destination = QtWidgets.QLabel(self.frame_save_destination)
        self.label_save_destination.setObjectName("label_save_destination")
        self.gridLayout_5.addWidget(self.label_save_destination, 0, 0, 1, 1)
        self.checkBox_save_destination = QtWidgets.QCheckBox(self.frame_save_destination)
        self.checkBox_save_destination.setMinimumSize(QtCore.QSize(128, 17))
        self.checkBox_save_destination.setMaximumSize(QtCore.QSize(128, 17))
        self.checkBox_save_destination.setObjectName("checkBox_save_destination")
        self.gridLayout_5.addWidget(self.checkBox_save_destination, 0, 1, 1, 1)
        self.lineEdit_save_destination = QtWidgets.QLineEdit(self.frame_save_destination)
        self.lineEdit_save_destination.setMinimumSize(QtCore.QSize(480, 20))
        self.lineEdit_save_destination.setMaximumSize(QtCore.QSize(480, 20))
        self.lineEdit_save_destination.setObjectName("lineEdit_save_destination")
        self.gridLayout_5.addWidget(self.lineEdit_save_destination, 1, 0, 1, 1)
        self.button_save_destination = QtWidgets.QToolButton(self.frame_save_destination)
        self.button_save_destination.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_save_destination.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.button_save_destination.setObjectName("button_save_destination")
        self.gridLayout_5.addWidget(self.button_save_destination, 1, 1, 1, 1, QtCore.Qt.AlignRight)
        self.gridLayout_4.addWidget(self.frame_save_destination, 4, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame_main)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_save_filename = QtWidgets.QLabel(self.frame_2)
        self.label_save_filename.setObjectName("label_save_filename")
        self.gridLayout.addWidget(self.label_save_filename, 0, 0, 1, 1)
        self.lineEdit_save_filename = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_save_filename.setObjectName("lineEdit_save_filename")
        self.gridLayout.addWidget(self.lineEdit_save_filename, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_2, 5, 1, 1, 1)
        self.button_live_basler = QtWidgets.QPushButton(self.frame_main)
        self.button_live_basler.setObjectName("button_live_basler")
        self.gridLayout_4.addWidget(self.button_live_basler, 7, 1, 1, 1)
        self.button_get_basler = QtWidgets.QPushButton(self.frame_main)
        self.button_get_basler.setObjectName("button_get_basler")
        self.gridLayout_4.addWidget(self.button_get_basler, 6, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 1, 1, 1, 1)
        self.label_image = QtWidgets.QLabel(self.frame_main)
        self.label_image.setText("")
        self.label_image.setObjectName("label_image")
        self.gridLayout_4.addWidget(self.label_image, 0, 1, 1, 1)
        self.gridLayout_12.addWidget(self.frame_main, 0, 0, 1, 1)
        self.frame_volume = QtWidgets.QFrame(self.centralwidget)
        self.frame_volume.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_volume.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_volume.setObjectName("frame_volume")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_volume)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_volume_title = QtWidgets.QLabel(self.frame_volume)
        self.label_volume_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_volume_title.setObjectName("label_volume_title")
        self.verticalLayout.addWidget(self.label_volume_title)
        self.tabwidget_volume = QtWidgets.QTabWidget(self.frame_volume)
        self.tabwidget_volume.setObjectName("tabwidget_volume")
        self.parameters_volume = QtWidgets.QWidget()
        self.parameters_volume.setObjectName("parameters_volume")
        self.formLayout = QtWidgets.QFormLayout(self.parameters_volume)
        self.formLayout.setObjectName("formLayout")
        self.widget_laser1 = QtWidgets.QWidget(self.parameters_volume)
        self.widget_laser1.setObjectName("widget_laser1")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.widget_laser1)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.checkBox_laser1 = QtWidgets.QCheckBox(self.widget_laser1)
        self.checkBox_laser1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_laser1.setObjectName("checkBox_laser1")
        self.gridLayout_8.addWidget(self.checkBox_laser1, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(145, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem2, 0, 1, 1, 2)
        self.slider_laser1 = QtWidgets.QSlider(self.widget_laser1)
        self.slider_laser1.setEnabled(False)
        self.slider_laser1.setOrientation(QtCore.Qt.Horizontal)
        self.slider_laser1.setObjectName("slider_laser1")
        self.gridLayout_8.addWidget(self.slider_laser1, 2, 1, 1, 1)
        self.spinBox_laser1 = QtWidgets.QSpinBox(self.widget_laser1)
        self.spinBox_laser1.setEnabled(False)
        self.spinBox_laser1.setObjectName("spinBox_laser1")
        self.gridLayout_8.addWidget(self.spinBox_laser1, 2, 0, 1, 1)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.widget_laser1)
        self.widget_laser2 = QtWidgets.QWidget(self.parameters_volume)
        self.widget_laser2.setObjectName("widget_laser2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.widget_laser2)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.checkBox_laser2 = QtWidgets.QCheckBox(self.widget_laser2)
        self.checkBox_laser2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_laser2.setObjectName("checkBox_laser2")
        self.gridLayout_9.addWidget(self.checkBox_laser2, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(76, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem3, 0, 1, 1, 2)
        self.slider_laser2 = QtWidgets.QSlider(self.widget_laser2)
        self.slider_laser2.setEnabled(False)
        self.slider_laser2.setOrientation(QtCore.Qt.Horizontal)
        self.slider_laser2.setObjectName("slider_laser2")
        self.gridLayout_9.addWidget(self.slider_laser2, 2, 1, 1, 1)
        self.spinBox_laser2 = QtWidgets.QSpinBox(self.widget_laser2)
        self.spinBox_laser2.setEnabled(False)
        self.spinBox_laser2.setObjectName("spinBox_laser2")
        self.gridLayout_9.addWidget(self.spinBox_laser2, 2, 0, 1, 1)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.widget_laser2)
        self.widget_laser3 = QtWidgets.QWidget(self.parameters_volume)
        self.widget_laser3.setObjectName("widget_laser3")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.widget_laser3)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.checkBox_laser3 = QtWidgets.QCheckBox(self.widget_laser3)
        self.checkBox_laser3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_laser3.setObjectName("checkBox_laser3")
        self.gridLayout_10.addWidget(self.checkBox_laser3, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(76, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem4, 0, 1, 1, 2)
        self.slider_laser3 = QtWidgets.QSlider(self.widget_laser3)
        self.slider_laser3.setEnabled(False)
        self.slider_laser3.setOrientation(QtCore.Qt.Horizontal)
        self.slider_laser3.setObjectName("slider_laser3")
        self.gridLayout_10.addWidget(self.slider_laser3, 2, 1, 1, 1)
        self.spinBox_laser3 = QtWidgets.QSpinBox(self.widget_laser3)
        self.spinBox_laser3.setEnabled(False)
        self.spinBox_laser3.setObjectName("spinBox_laser3")
        self.gridLayout_10.addWidget(self.spinBox_laser3, 2, 0, 1, 1)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.widget_laser3)
        self.widget_laser4 = QtWidgets.QWidget(self.parameters_volume)
        self.widget_laser4.setObjectName("widget_laser4")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.widget_laser4)
        self.gridLayout_11.setObjectName("gridLayout_11")
        spacerItem5 = QtWidgets.QSpacerItem(76, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem5, 0, 1, 1, 2)
        self.checkBox_laser4 = QtWidgets.QCheckBox(self.widget_laser4)
        self.checkBox_laser4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_laser4.setObjectName("checkBox_laser4")
        self.gridLayout_11.addWidget(self.checkBox_laser4, 0, 0, 1, 1)
        self.slider_laser4 = QtWidgets.QSlider(self.widget_laser4)
        self.slider_laser4.setEnabled(False)
        self.slider_laser4.setOrientation(QtCore.Qt.Horizontal)
        self.slider_laser4.setObjectName("slider_laser4")
        self.gridLayout_11.addWidget(self.slider_laser4, 1, 1, 1, 1)
        self.spinBox_laser4 = QtWidgets.QSpinBox(self.widget_laser4)
        self.spinBox_laser4.setEnabled(False)
        self.spinBox_laser4.setObjectName("spinBox_laser4")
        self.gridLayout_11.addWidget(self.spinBox_laser4, 1, 0, 1, 1)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.widget_laser4)
        self.label_slice_distance = QtWidgets.QLabel(self.parameters_volume)
        self.label_slice_distance.setObjectName("label_slice_distance")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_slice_distance)
        self.label_slice_number = QtWidgets.QLabel(self.parameters_volume)
        self.label_slice_number.setObjectName("label_slice_number")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_slice_number)
        self.label_exposure = QtWidgets.QLabel(self.parameters_volume)
        self.label_exposure.setObjectName("label_exposure")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_exposure)
        self.lineEdit_exposure = QtWidgets.QLineEdit(self.parameters_volume)
        self.lineEdit_exposure.setObjectName("lineEdit_exposure")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lineEdit_exposure)
        self.lineEdit_slice_number = QtWidgets.QLineEdit(self.parameters_volume)
        self.lineEdit_slice_number.setObjectName("lineEdit_slice_number")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_slice_number)
        self.lineEdit_slice_distance = QtWidgets.QLineEdit(self.parameters_volume)
        self.lineEdit_slice_distance.setObjectName("lineEdit_slice_distance")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_slice_distance)
        self.tabwidget_volume.addTab(self.parameters_volume, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_13.addWidget(self.lineEdit_4, 0, 1, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_13.addWidget(self.lineEdit_6, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_13.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_13.addWidget(self.label_6, 1, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_13.addWidget(self.lineEdit_5, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_13.addWidget(self.label_7, 2, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_13.addItem(spacerItem6, 3, 0, 1, 1)
        self.tabwidget_volume.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabwidget_volume)
        self.pushButton_volume = QtWidgets.QPushButton(self.frame_volume)
        self.pushButton_volume.setFlat(False)
        self.pushButton_volume.setObjectName("pushButton_volume")
        self.verticalLayout.addWidget(self.pushButton_volume)
        self.frame = QtWidgets.QFrame(self.frame_volume)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lineEdit_move_absolute = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_move_absolute.setObjectName("lineEdit_move_absolute")
        self.gridLayout_6.addWidget(self.lineEdit_move_absolute, 2, 1, 1, 1)
        self.pushButton_move_relative = QtWidgets.QPushButton(self.frame)
        self.pushButton_move_relative.setObjectName("pushButton_move_relative")
        self.gridLayout_6.addWidget(self.pushButton_move_relative, 3, 0, 1, 1)
        self.pushButton_move_absolute = QtWidgets.QPushButton(self.frame)
        self.pushButton_move_absolute.setObjectName("pushButton_move_absolute")
        self.gridLayout_6.addWidget(self.pushButton_move_absolute, 2, 0, 1, 1)
        self.lineEdit_move_relative = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_move_relative.setObjectName("lineEdit_move_relative")
        self.gridLayout_6.addWidget(self.lineEdit_move_relative, 3, 1, 1, 1)
        self.pushButton_initialise_stage = QtWidgets.QPushButton(self.frame)
        self.pushButton_initialise_stage.setObjectName("pushButton_initialise_stage")
        self.gridLayout_6.addWidget(self.pushButton_initialise_stage, 1, 0, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem7, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.gridLayout_12.addWidget(self.frame_volume, 0, 1, 1, 1)
        MainGui.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainGui)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 852, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainGui.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainGui)
        self.statusbar.setObjectName("statusbar")
        MainGui.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainGui)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainGui)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainGui)
        self.tabwidget_volume.setCurrentIndex(0)
        self.spinbox_slider.valueChanged['int'].connect(self.slider_stack.setValue)
        self.slider_stack.valueChanged['int'].connect(self.spinbox_slider.setValue)
        self.spinBox_laser1.valueChanged['int'].connect(self.slider_laser1.setValue)
        self.slider_laser1.valueChanged['int'].connect(self.spinBox_laser1.setValue)
        self.spinBox_laser2.valueChanged['int'].connect(self.slider_laser2.setValue)
        self.slider_laser2.valueChanged['int'].connect(self.spinBox_laser2.setValue)
        self.spinBox_laser3.valueChanged['int'].connect(self.slider_laser3.setValue)
        self.slider_laser3.valueChanged['int'].connect(self.spinBox_laser3.setValue)
        self.spinBox_laser4.valueChanged['int'].connect(self.slider_laser4.setValue)
        self.slider_laser4.valueChanged['int'].connect(self.spinBox_laser4.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainGui)

    def retranslateUi(self, MainGui):
        _translate = QtCore.QCoreApplication.translate
        MainGui.setWindowTitle(_translate("MainGui", "MainWindow"))
        self.label_slider.setText(_translate("MainGui", "Stack Slider"))
        self.label_save_destination.setText(_translate("MainGui", "Save Destination"))
        self.checkBox_save_destination.setText(_translate("MainGui", "Lock Save Destination"))
        self.button_save_destination.setText(_translate("MainGui", "..."))
        self.label_save_filename.setText(_translate("MainGui", "Save Filename"))
        self.button_live_basler.setText(_translate("MainGui", "Live Basler View"))
        self.button_get_basler.setText(_translate("MainGui", "Get Basler Image"))
        self.label_volume_title.setText(_translate("MainGui", "Volume Acquisition"))
        self.checkBox_laser1.setText(_translate("MainGui", "Laser 1"))
        self.checkBox_laser2.setText(_translate("MainGui", "Laser 2"))
        self.checkBox_laser3.setText(_translate("MainGui", "Laser 3"))
        self.checkBox_laser4.setText(_translate("MainGui", "Laser 4"))
        self.label_slice_distance.setText(_translate("MainGui", "Slice Distance"))
        self.label_slice_number.setText(_translate("MainGui", "Number of Slices"))
        self.label_exposure.setText(_translate("MainGui", "Exposure Time (s)"))
        self.tabwidget_volume.setTabText(self.tabwidget_volume.indexOf(self.parameters_volume), _translate("MainGui", "Parameters"))
        self.label_5.setText(_translate("MainGui", "Reading Pause"))
        self.label_6.setText(_translate("MainGui", "Accuracy Threshold"))
        self.label_7.setText(_translate("MainGui", "Threshold Steps"))
        self.tabwidget_volume.setTabText(self.tabwidget_volume.indexOf(self.tab_2), _translate("MainGui", "Settings"))
        self.pushButton_volume.setText(_translate("MainGui", "Acquire Volume"))
        self.pushButton_move_relative.setText(_translate("MainGui", "Move Relative"))
        self.pushButton_move_absolute.setText(_translate("MainGui", "Move Absolute"))
        self.pushButton_initialise_stage.setText(_translate("MainGui", "Initialise Stage"))
        self.menuFile.setTitle(_translate("MainGui", "File"))
        self.actionOpen.setText(_translate("MainGui", "Open"))
        self.actionSave.setText(_translate("MainGui", "Save"))
