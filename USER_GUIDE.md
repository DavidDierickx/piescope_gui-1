After using the PIE-scope GUI please remember to properly [close](#closing-down) hardware connections and software before leaving.
----
## Contents ##

- [**Getting Started**](#getting-started)
  - [**Hardware connections**](#hardware-connections)
  - [**Opening the GUI**](#opening-the-gui)
- [**GUI Operations**](#gui-operations)
  - [**Imaging**](#imaging)
  - [**Stage movement**](#stage-movement)
  - [**Additional functions**](#additional-functions)
- [**Closing down**](#closing-down)
- [**Troubleshooting**](#troubleshooting)


------------------------------------------------------------------------------------

# GETTING STARTED #

------------------------------------------------------------------------------------

# Hardware connections #

------------------------------------------------------------------------------------


There are a few hardware connections that need to be made before you can operate the GUI.  

**Lasers**

- Make sure the lasers are powered.
- Make sure that the lasers are connected via USB to the PFIB2 computer.
- <!SHOW IMAGE
- Turn the key to turn the lasers on as shown in the image below.
- <!SHOW IMAGE

**Basler detector**

- Make sure the box <!-- (IMAGE) -->has power
- Ensure the detector is connected to the PFIB2 computer via ethernet cord
- <!Image
- Check that the stage is installed properly in the PIEscope 
- <!Image
- Check that the imaging detector is connected to the PFIB2 via USB.
- <!Image

Note: Remember to [close down](#closing-down) the hardware before leaving the room.

# Opening the GUI #

------------------------------------------------------------------------------------

note - add milling from main

- Log into the admin account on PFIB2
- Open Start Menu
- Type in "*Anaconda*"
- Press enter
- In the command prompt type:
	1. "*conda activate piescope-dev*"
	2. "*cd Github*"
	3. "*cd piescope_gui*"
	4. "*cd piescope_gui*"
	5. "*piescope*" OR "*python main.py*"
	
<!--**INSERT IMAGE OF GUI**_____________________!!!!!!!!!!!!!!!!-->

----
----
# GUI OPERATIONS #

------------------------------------------------------------------------------------

## Contents ##

[**Imaging**](#imaging)
- [Fluorescence microscope](#fluorescence-microscope)
- [Electron microscope](#electron-microscope)
- [Ion beam](#ion-beam)

[**Stage movement**](#stage-movement)
- [Sample stage](#sample-stage)
- [Objective stage](#objective-stage)

[**Additional functions**](#additional-functions)
- [Fluorescence volume acquisition](#fluorescence-volume-acquisition)
- [Image correlation](#image-correlation)
- [Milling](#milling)


# Imaging #
----

## Fluorescence Microscope ##


<!--INSERT IMAGE OF FM SECTION-->

**Taking images**

<!--INSERT IMAGE OF IMAGE BUTTONS-->

*Note:*  Ensure to check settings before taking images

To take a single basler image simply press the "Get Basler Image" Button.  

To conduct live imaging press the "Live Basler View" button.  In order to stop live imaging press this button again.  Live imaging is used to focus the fluorescence imaging detector.

**Settings**

<!--INSERT IMAGE OF FILE SAVING SECTION-->

File saving settings are changed in the top section of the Fluorescence Microscope Section (FM):

To change the folder in which fluorescence images are saved you can either manually enter the save path folder or press the [ ... ] button to navigate to the desired folder [Dark Blue].

*Note*:  In order to use the [ ... ] button the "Lock Save Destination" button must be unchecked.

To change the save filename manually enter the desired name in the "Save Filename" box [Dark Green].

<!--INSERT IMAGE OF IMAGING PARAMETER SECTION-->

Imaging parameters are changed in the bottom section [Orange].

First choose the laser wavelength (Available options are 640nm, 561nm, 488nm, 
405nm) from the drop down menu on the left.  

Then enter the desired power level as a percentage (Integer with range from 0-100).

Finally set the exposure time in ms.

## Electron Microscope ##

<!--INSERT IMAGE OF FIBSEMM SECTION-->

#### Taking images ####

<!--INSERT IMAGE OF IMAGE BUTTONS-->

*Note:*  Ensure to check settings before taking images

To take a new electron image press the "Get SEM Image" Button.

To grab the last taken electron image press the "Grab Last SEM" Button.

**Settings**

<!--INSERT IMAGE OF FILE SAVING SECTION-->

File saving settings are changed in the top section of the Scanning Electron Microscope Section (FIBSEM):

To change the folder in which the electron microscope images are saved you can either manually enter the save path folder or press the [ ... ] button to navigate to the desired folder [Dark Blue].

**Note**:  In order to use the [ ... ] button the "Lock Save Destination" button must be unchecked.

To change the save filename manually enter the desired name in the "Save Filename" box [Dark Green].

<!--INSERT IMAGE OF IMAGING PARAMETER SECTION-->

Imaging parameters are changed in the bottom right section [Orange].

Dwell time is set in microseconds as integer value in the corresponding text box.

When the autocontrast box is ticked the scanning electron microscope will perform an autocontrast before taking an image.

The image resolution can be selected from the drop down box.



## Ion beam ##


<!--INSERT IMAGE OF FIBSEMM SECTION-->

**Taking images**
<!--INSERT IMAGE OF IMAGE BUTTONS-->

*Note:*  Ensure to check settings before taking images

To take a new electron image press the "Get FIB Image" Button.

To grab the last taken electron image press the "Grab Last FIB" Button.

**Settings**

<!--INSERT IMAGE OF FILE SAVING SECTION-->

File saving settings are changed in the top section of the Focused Ion Beam/Scanning Electron Microscope Section (FIBSEM):

To change the folder in which focused ion beam images are saved you can either manually enter the save path folder or press the [ ... ] button to navigate to the desired folder [Dark Blue].

**Note**:  In order to use the [ ... ] button the "Lock Save Destination" button must be unchecked.

To change the save filename manually enter the desired name in the "Save Filename" box [Dark Green].

<!--INSERT IMAGE OF IMAGING PARAMETER SECTION-->

Imaging parameters are changed in the bottom right section [Orange].

Dwell time is set in microseconds as integer value in the corresponding text box.

When the autocontrast box is ticked the focused ion beam will perform an autocontrast before taking an image.

The image resolution can be selected from the drop down box.

# Stage movement
----

## Sample stage ##


<!--INSERT IMAGEE-->

The sample stage controls are towards the bottom left corner of the GUI.

When you are at the location of the FIBSEM and wish to go to the FM click the "To Light Microscope" Button.

When you are at the location of the FM and wish to go to the FIBSEM click the "To Electron Microscope" Button.

## Objective stage ##


<!--INSERT IMAGEE-->

**Positioning**

The objective stage controls are in the bottom left corner of the GUI.

To send the objective stage back to its center press the "Initialise Stage" button.

To read the current position of the objective stage press the "Get Position" button.

To save the current position of the objective stage press the "Save Position" button.

When you have saved a position you can travel back to this position using the "Go to saved position" button.

**Movement**

To make an absolute movement enter the distance in micrometers in the text box and press the "Move Absolute (um)" button.

To make a relative movement enter the distance in micrometers in the text box and press the "Move Relative (um)" button.



# Additional functions
------------------------------------------------------------------------------------

## Fluorescence volume acquisition

**Lasers**

<!--ADD Image-->

The controls for the lasers to be used during volume acquisition are located in the top left corner of the GUI.  

Selecting a laser is done by checking the box located next to the corresponding laser wavelength.  To deselect a laser simply uncheck this box.

Once a lase is selected, the exposure time for images taken whilst that laser is on can be chosen by manually entering the time (in milliseconds) in the text box.

To change the power level of the selected laser you can either drag the corresponding slider or enter the power level manually in the box on the left.  For fine adjustments the two arrows attached to the power level box can be used to change the power level 1 percent at a time.

**Settings**

Once the lasers and their corresponding exposure times and power levels have been selected, the distance between each slice of the volume and the amount of slices to be taken must be entered into their corresponding text boxes.  The slice distance is given in nanometers and the amount of slices is an integer.

**Taking a volume**
Once all of these parameters have been selected simply click the "Acquire Volume" button and the system will take all of the required images with each laser wavelength.


## Image correlation

**Preparation**
First ensure there is an image currently loaded/taken for both the FM and FIBSEM.  

If you don't have the desired images see:
- [Fluorescence imaging](#fluorescence-microscope)
- [Electron imaging](#electron-microscope)
- [Ion beam imaging](#ion-beam)


Then, under the correlation button <!--[show image]-->,  select the path to which the output correlated image will be saved to.  This can be done by manually entering the path in the text field or by clicking on the [ ... ] button and navigating to the desired path.

**Correlation**

Once the preparation is complete click the "Correlation" button <!--(IMAGE)--> which will open the [Control Point Selection Tool](#image-correlation).

<!--Show Image-->

This window places the two images to correlate side by side.  There are controls to interact with the images, such as zooming and panning, in the top left corner.  

A help dialogue is located in the top right corner to guide you through the point selection process.

Correlation is done by clicking on control points in each image that correspond to the same location.    

Once correlation is complete and the "Return" button is clicked, the [Milling Parameter Selection](#milling) window will be opened. 


## Milling 

<!--Image of window-->

The Milling Parameter Window shows the overlaid image of the correlation of two images completed in the [Control Point Selection Tool](#image-correlation).

**Creation of milling pattern**

To create a rectangular milling pattern simply click and drag from the top left corner of the desired rectangle to the bottom left corner.

Once satisfied with the rectangle press the "Send milling pattern to FIBSEM" button to send the pattern to the FIBSEM controller.

**Milling control**

Milling of the rectangular pattern sent to the FIBSEM can be controlled by starting, pausing and stopping.  

To start milling with the pattern sent to the FIBSEM, press the "Start milling pattern" button.  

To pause the milling operation in progress, press the "Pause milling pattern" button.

To completely stop the milling process, press the "Stop milling pattern" button.

When done with milling, press the "Exit" button to return to the GUI main window.

----
# CLOSING DOWN 
----
Before leaving please remember to properly close hardware connections and software.

Make sure each of these steps is completed:  
- Turn off lasers <!--(IMAGE)-->
- Put the FIBSEM to sleep <!--(IMAGE)-->
- Log out of PFIB2

------------------------------------------------------------------------------------
# TROUBLESHOOTING #
------------------------------------------------------------------------------------
## Opening GUI

If you are having trouble with opening the GUI, check that you have the correct envireonment enable in Anaconda.  This can be seen by the name in brackets to the left of each line <!--(IMAGE).-->

Also check that you are in the correct location for opening the GUI, which is the folder "Admin/Github/Piescope_GUI/Piescope_GUI".  This can be seen here <!--(IMAGE)-->


## Operation errors

If an error is thrown whilst operating the GUI, first ensure that each piece of hardware is properly connected as per [Hardware connections](#hardware-connections).


**Lasers**

An issue that can be encountered when communicating with the laser control hardware is that another program is currently controlling the lasers.  The most common cause of this is that Toptica is connected to the lasers.  This can be checked by opening the Toptica application by going to the start menu, typing "Topas" and pressing enter.  If the application is connected to the lasers, as shown in the image below, click "disconnect" under MENU. <!--(IMAGES).-->

You should now be able to connect to the lasers properly.

**Basler**

If communicaton to the Basler fails it is possibly an IP address problem.  

This can be checked by opening the ASCII Terminal by going to the start menu and typing "ASCII" and pressing enter.

Go to EDIT/SETTINGS then 
Here make sure that the Network Configuration under the "Connection" tab is given as 169.254.111.111, port 139

Click the "Connect" button under the """" Tab.

If connection is successful type GSI into the text box and press "Send Command".  

If the Basler is properly connected the output should be ":ID4050785033", otherwise if the Basler is not connected properly a diamond with a question mark will be the output.

**Checking IP address**

To check the IP address used to connect to the basler:
1. Go to the Start Menu
2. Type "View Network Connectons"
3. Press enter.  
4. Right click on "Ethernet 2" and press "Properties".  
5. Under the "This connection uses the following items" line, navigate to "Internet Protocol Version 4 (TCP/IPv4)
6. Click properties.
7. Click "Use the following IP address:" if it is not already selected.
8. Check/change the values:
  ```
  IP address: 169.254.111.112
  Subnet Mask: 255.255.255.192
  Default Gateway: Blank
  ```
9. Press OK.

