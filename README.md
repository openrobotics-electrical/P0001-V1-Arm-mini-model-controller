# P0001-V1-Arm-mini-model-controller
Scale model of V1 robot arm, human interface device for testing arm control

Summary
This project is a miniaturized scale model of the @Home V1 robot arm for the purpose of testing arm control software. The model contains several potentiometers to measure position/angle, and buttons on the “hand” to manipulate the end affector. This circumvents the need for advanced inverse kinematics or control software and lets the developer focus on just getting the arm to work before working on those. 

Jun 7: wire connecting pull down resistor to end affector control button is broken.

 
Features
Joint pieces are 3D printed, held together by alignment pins and a single screw and captive nut each. Arm links are thin laser cut acrylic, fit onto the pins. Potentiometers (see datasheet) are actuated by square 1/8” shafts pegged into the 3D printed joints or slotted into a square hole on the arm linkages. The end affector button is a 6x6mm through hole button with a 10k pull down to ground. The base is laser cut wood, glued together

Analog signals from the potentiometer are sent to the Arduino, which also provides 5V/GND to the potentiometers and button. The Arduino code polls the potentiometers and sends them over serial (9600 baud, 8N1) to the computer. See the code for potentiometer analog value mapping to angle/position. Example Python code parses incoming serial data and maps it to the servo control.

Current limitations
The wire channels in the joint pieces are undersized for standard 22ga wire, and require the potentiometer power/ground to be daisy chained. 

Arduino code constantly sends serial data to computer instead of when asked for them, so the serial buffer can be filled up, and must be cleared to get the latest data. 
