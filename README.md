# IoT
# Components Required:
- Raspberry Pi Pico with USB Connection to PC
- Breadboard
- RAK4270 with Antenna
- LED
- Analogue Joystick
- Light Depenedant Resistor (LDR) / Photo-Resistor
- Ultrasonic Sensor (HC-SR04)
- Particle Matter Sensor (PMD5003)
- 10 kiloohm Resistor
- 220 ohm Resistor
- 14 F-M Cables Maximum
- 7 M-M Cables Maximum
# Software Used:
- Chrome
- Thonny
- GitHub
# Programming Process
# LED Process
To begin with I started with a very basic circuit containing the Raspberry Pi Pico, LED, and 220 ohm resistor all plugged into the breadboard. I then wrote the code to blink the LED on and off. Following this I developed both the circuit and code further by adding in a button, which was then used as a condition in a selection statement with the code to toggle the LED nested in it. Further advancements were made by implemeting the ability for the LED to change its brightness, via the implementation of pulse-width modulation (PWM). Finally I replaced the button with an analogue joystick and used this to change the brightness of the LED based upon the X value of the joystick after an analogue to digital converter (ADC) had been applied to it.
# LoRa Transmission, via the RAK module.
# Use of The Things Network
I created an account with The Things Network and was then invited to join an application where I could transmit my data to. I also coded my own payload formatter in JavaScript so that the data could be converted into a more readable format, for human users. Finally I created a webhook to Datacake, so that the data could be uplinked and stored in Datacake
# Use of Datacake
I created an account with Datacake and was then invited to join the Blenheim workspace. I created another, similar, payload formatter on Datacake and finally created fields for my data to be stored in.
# Light Dependant Resistor (LDR)/Photo-Resistor Process
My initial use of the RAK module to transmit data from sensors was with an LDR measuring the surrounding light levels. I applied an ADC to the readings from the LDR and converted this value to a percentage. I then used a while loop to constantly check the value of the LDR, adn used an if statement to check if it went below 20%. If this condition was met the data would be transmitted to The Things Network and uplinked to Datacake. The uses of a program such as this could be automating lights turning on or off if a certain light level is reached; this may help save energy because it would prevent lights being left on when they are not needed.
# Ultrasonic Sensor Process
After using the LDR I moved onto using an ultrasonic sensor, in a similar fashion to how I used the LDR. I created an algorithm to convert the time taken, for the sound to be emitted from the sensor and reflect back off of an object, into a distance - in centimeters - by using the speed of sound in air and this time in the equation: distance = speed x time. Using this algorithm I was able to check whether an object was closer to the sensor than a set distance, I chose 15cm, and transmit the value of the distance to The Things Network and Datacake. Uses of this system involve: water level detection and detecting if people are too close to historic artifacts.
