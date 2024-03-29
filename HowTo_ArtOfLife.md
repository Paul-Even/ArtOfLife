# ART OF LIFE - Documentation
<p align="center">
<img src="https://github.com/Paul-Even/ArtOfLife/assets/114758201/bc58b096-c290-4f04-b164-9dc7108552ce" height="500">
</p>

## 0. Everything necessary for this project

### Hardware :

1. Plux Biosignals ECG Sensor : https://www.pluxbiosignals.com/products/electrocardiography-ecg-sensor?variant=40878841200831
2. Plux Biosignals EDA Sensor : https://www.pluxbiosignals.com/products/electrodermal-activity-eda-sensor
3. Plux Biosignals Breathing Sensor : https://www.pluxbiosignals.com/products/respiration-pzt
4. Plux Biosignals Bitalino card : https://www.pluxbiosignals.com/products/bitalino-revolution-plugged-kit-ble-bt
5. 5 electrodes : https://www.pluxbiosignals.com/products/gelled-self-adhesive-disposable-ag-agcl-electrodes

### Softwares : 

6. Visual Studio Code
7. FL Studio
8. MadMapper
9. loopMIDI

## 
## 1. Putting the sensors on the user
###    a. ECG Sensor

This sensor uses three electrodes placed on the user’s upper body (see Figure 1). You must connect the three electrodes to the sensor to ensure qualitative data. The reference electrode can be placed around the left lowest rib for an easier installation.



<p align="center"><img src="https://github.com/Paul-Even/ArtOfLife/assets/114758201/7cd4c20e-ed4d-4986-a90b-813919e9a522" height="500"> 
<img src="https://github.com/Paul-Even/ArtOfLife/assets/114758201/eb13e8f2-bf3c-46b4-80f6-c3e1b9c5cd9d" height="150">


</p>
<p align="center">
    <a>
      Figure 1 : Positioning of the 3 electrodes relative to the ECG Sensor.
  
</p>
<br/>
<br/>

###    b. EDA Sensor

This sensor uses two electrodes placed on one of the user’s hands (see Figure 2). You must connect the two electrodes to ensure qualitative data. 

<p align="center">
  <img src="https://github.com/Paul-Even/ArtOfLife/assets/114758201/3170627b-215b-486f-98e3-9a87ea64f061" height ="500">

</p>

<p align="center">
    <a>
      Figure 2 : Positioning of the two electrodes relative to the EDA Sensor.

    
</p>
<br/>
<br/>

###    c. Breathing Sensor

This sensor uses a stretchable band that must be placed around the user’s ribs and will detect when the user inhales and exhales.

<p align="center">
  <img src="https://github.com/Paul-Even/ArtOfLife/assets/114758201/82219cb8-46b6-43b2-bd5b-9ccd1907622f" height ="500">
</p>
<p align="center">
    <a>
      Figure 3 : Positioning of the breathing sensor’s stretchable band.
</p>
<br/>
<br/>

## 
## 2. Bitalino card & OpenSignals

###    a. Connecting the sensors to the Bitalino card

The Bitalino card (see Figure 4) is responsible for gathering all the data from the three sensors and sending them to the OpenSignals software. The card possesses multiple ports beginning with “A”, being the ones which the sensors need to be connected to.\
Make sure to connect the ECG Sensor to “A1”, the EDA Sensor to “A2” and the Breathing Sensor to “A3”. Then, turn on the card so it can connect to the OpenSignals software by Bluetooth.

<p align="center">
  <img src="https://github.com/Paul-Even/ArtOfLife/assets/114758201/72cd3280-59b5-45cf-99ae-ea8b854d21e9" height="300"
</p>
<p align="center">
    <a>
      Figure 4 : The Bitalino card.
</p>
<br/>
<br/>
      
###    b. Visualizing the data on OpenSignals

The OpenSignals software helps visualize the sensors’ data and send it to an external python program. These results need multiple actions to be done. Firstly, you need to connect the software to the card, then you can select which ports are connected to which sensors (see Figure 5).

<p align="center">
  <img src="https://github.com/Paul-Even/ArtOfLife/assets/114758201/3efae4d2-f1ef-4ea6-8e25-0f249419d1e1" height ="300">
</p>
<p align="center">
    <a>
      Figure 5 : Connection to the Bitalino card and selecting the sensors on the OpenSignals software.
</p>
<br/>
<br/>

###    c. Sending the data to the Python program

The sensor data can be sent to a Python program using the Lab Streaming Layer. To do so, you need to activate the “Lab Streaming Layer” parameter in the “Integration” section of the settings (the button next to the one used for connecting to the Bitalino card).

## 
## 3. Python & loopMIDI

###    a. The Python program

The Python program is responsible for converting the raw data into MIDI notes. For this purpose, the program receives the values from OpenSignals and detects when a pulse is happening or if the user is inhaling or exhaling. During these events, the program sends different MIDI notes to multiple programs to impact the music and the visuals displayed. This program is called "ArtOfLife.py" and can be found on this GitHub repository. But before running the program, we must create virtual MIDI ports.

<br/>
<br/> 

###    b. loopMIDI

For the Python program to be able to send MIDI notes, the computer needs to open virtual MIDI ports to receive the notes, and so is the role of loopMIDI. loopMIDI is a very simplistic software that can open personalized MIDI ports. You will need to create two ports that will link to the FL Studio software. Make sure to call them “loopMIDI Port FL” and “loopMIDI Port FL2”. Then, you must connect one port related to the MadMapper software. Make sure to call it “loopMIDI Port MM”. Only after that you can start running the Python program.

<p align="center">
  <img src="https://github.com/Paul-Even/ArtOfLife/assets/114758201/fa07612d-41a4-46f3-9eab-560baf81a0e6" height ="300">
</p>
<p align="center">
    <a>
      Figure 6 : Created ports on loopMIDI.
</p>
<br/>
<br/>

## 
## 4. FL Studio 20

FL Studio 20 is the music software used in this project. The software will play a predefined looped sample of music while displaying sounds reacting to the MIDI notes it receives from loopMIDI. The FL Studio file is called “ArtOfLife.flp” and can be found on this GitHub repository.
To make sure the project is well connected to the MIDI ports, you can go to “Options > MIDI Settings” and see if the two MIDI ports are listed and activated as inputs 1 and 2 (see Figure).
Don’t forget to press play; otherwise, no music will play!

<p align="center">
  <img src="https://github.com/Paul-Even/ArtOfLife/assets/114758201/4b389029-4b8c-4cd2-ab08-ce318dd1188a" height ="125">
</p>
<p align="center">
    <a>
      Figure 7 : Activating the MIDI ports as inputs on FL Studio.
</p>
<br/>
<br/>

## 
## 5.MadMapper

MadMapper (version 5.0.7) is the video-mapping software used in this project. The software will display predefined shaders which will react to the MIDI notes it receives from loopMIDI. The MadMapper file is called “ArtOfLife.mad” and can be found on this GitHub repository. 

<p align="center">
  <img src="assets/MadInterface.PNG" height ="125">
</p>
<p align="center">
    <a>
      Figure 8 : ArtofLife MadMapper Interface.
</p>


To ensure that the visual is displayed with the projector, once it is connected to your computer, make sure to set the "extend display" mode in your computer settings. Then click on the following icon, top left in madmapper :

<p align="center">
  <img src="assets/projectorsetup1.PNG" height ="125">
</p>
<p align="center">
    <a>
      Figure 9 : Projector Icon.
</p>

Then click on "Video-output-1" and a new table with more information will appear at bottom left. Click on "Desktop Window" 

<p align="center">
  <img src="assets/Desktop window.PNG" height ="125">
</p>
<p align="center">
    <a>
      Figure 10 : Desktop Window Button.
</p>

This button lets you load a new window that you'll need to place on your "second screen", i.e. whatever the projector is projecting.

Now the visual projection is all set ! But let's make sure that the midi port are well connected to it.

<br/>
