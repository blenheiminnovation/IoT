# IoT
# Software Used:
- Chrome
- Thonny
- GitHub
# Programming Process
## LED Process
### Components Required: ###
- Raspberry Pi Pico with USB Connection to PC
- Breadboard
- LED
- Analogue Joystick
- 220 ohm Resistor
- 5 M-M Cables
- 5 F-M Cables

To begin with you should start with a very basic circuit containing the Raspberry Pi Pico, LED, and 220 ohm resistor all plugged into the breadboard. You should then write the code to blink the LED on and off. Following this you can develop both the circuit and code further by adding in a button, which is then used as a condition in a selection statement with the code to toggle the LED nested in it. Further advancements are made by implemeting the ability for the LED to change its brightness, via the implementation of pulse-width modulation (PWM). Finally you could replace the button with an analogue joystick and use this to change the brightness of the LED based upon the X value of the joystick after an analogue to digital converter (ADC) had been applied to it.
## LoRa Transmission, via the RAK module.
### Overarching Themes ###
For all of the following programs you will need the following modules:
- machine
- time
- utime
- struct
- binascii - to convert strings into hexadecimal

All of the payloads are in the format: Sensor Type, Sensor Name, Value 1, Value2, and Value 3. However the fields Value 2 and Value 3 were only required for the particulate matter sensor, so can be left blank in the other programs.
### Use of The Things Network ###
You need to create an account with The Things Network and was then join an application where you can transmit data to. You also need to code your own payload formatter in JavaScript so that the data could be converted into a more readable format, for human users. Finally create a webhook to Datacake, so that the data can be uplinked and stored in Datacake. To find your DevEUI, AppEUI, and AppKey you must go into the 'End devices' section of your application; then you need to click on your device and under the 'Activation information' subheading you should see the DevEUI, AppEUI, and AppKey.
### Use of Datacake ###
You will have to create an account with Datacake and was then invited to join the Blenheim workspace. You will have to create another, similar, payload formatter on Datacake and finally create fields for your data to be stored in.
### Light Dependant Resistor (LDR)/Photo-Resistor Process ###
#### Components Required ####
- Raspberry Pi Pico with USB Connection to PC
- Breadboard
- RAK4270 with Antenna
- Light Depenedant Resistor (LDR) / Photo-Resistor
- 10 kiloohm Resistor
- 2 M-M Cables
- 4 F-M Cables

The initial use of the RAK module to transmit data from sensors can be with an LDR measuring the surrounding light levels. You need to apply an ADC to the readings from the LDR and convert this value to a percentage, for easier handling. Then use a while loop to constantly check the value of the LDR, and use an if statement to check if it goes below 20%. If this condition is met the data will be transmitted to The Things Network and uplinked to Datacake. The uses of a program such as this could be automating lights turning on or off if a certain light level is reached; this may help save energy because it would prevent lights being left on when they are not needed.
### Ultrasonic Sensor Process ###
#### Components Required ####
- Raspberry Pi Pico with USB Connection to PC
- Breadboard
- RAK4270 with Antenna
- Ultrasonic Sensor (HC-SR04)
- 4 M-M cables
- 8 F-M Cables

After using the LDR you may want to move onto using an ultrasonic sensor, in a similar fashion to how you used the LDR. You need to create an algorithm to convert the time taken, for the sound to be emitted from the sensor and reflect back off of an object, into a distance - in centimeters - by using the speed of sound in air and this time in the equation: distance = speed x time. Using this algorithm you are able to check whether an object was closer to the sensor than a set distance, for example 15cm, and transmit the value of the distance to The Things Network and Datacake. Uses of this system involve: water level detection and detecting if people are too close to historic artifacts.
### Particulate Matter Sensor Process ###
#### Components Required ####
- Raspberry Pi Pico with USB Connection to PC
- Breadboard
- RAK4270 with Antenna
- Particulate Matter Sensor (PMS5003) and Breakout Board
- 8 F-M Cables

Using the knowledge you have acquired from all of the previous sensors and programs you will be able to connect a particulate matter sensor (PMS) to the raspberry Pi Pico and RAK module and constantly monitor the surrounding air and transmit this data every minute. You will have to install two modules, being: pms5003-micropython and micropython-uasyncio, however the implementation of these modules allow you to read the data from the PMS and then transmit this data to The Things Network and Datacake. This has uses within many settings, such as offices, classrooms, and homes because it allows users to see if the air surrounding them is safe which means health risks are minimised.

