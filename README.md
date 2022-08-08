# IoT

## Software Used:

- Chrome
- Thonny
- GitHub

## Programming Process

### LED Process

#### Components Required:

- Raspberry Pi Pico with USB Connection to PC
- Breadboard
- LED
- Analogue Joystick
- 220 ohm Resistor
- 5 M-M Cables
- 5 F-M Cables

To begin with you could start with a very basic circuit containing the Raspberry Pi Pico, LED, and 220 ohm resistor all plugged into the breadboard. You should then write the code to blink the LED on and off. Following this you can develop both the circuit and code further by adding in a button, which is then used as a condition in a selection statement with the code to toggle the LED nested in it. Further advancements are made by implemeting the ability for the LED to change its brightness, via the use of pulse-width modulation (PWM). Finally you could replace the button with an analogue joystick and use this to change the brightness of the LED based upon the X value of the joystick after an analogue to digital converter (ADC) had been applied to it.

### LoRa Transmission, via the RAK module.

#### Overarching Themes

For all of the following programs you will need the following modules:

- machine
- time
- utime
- struct
- binascii - to convert strings into hexadecimal

All of the payloads are in the format: Sensor Type, Sensor Name, Value 1, Value2, and Value 3. However the fields Value 2 and Value 3 were only required for the particulate matter sensor, so can be left blank in the other programs.

#### Setting up Thonny

Firstly you will need to download the Thonny IDE, in order to be able to write code for the Raspberry Pi Pico to execute. Once you have succesfully downloaded and installed Thonny, plug your Raspberry Pi Pico into the computer - whilst holding the BOOTSEL button, and press the Stop/Restart button at the top of the Thonny window; a window should pop up allowing you to install MicroPython firmware to the Raspberry Pi Pico. Make sure the target device is correct and press install, once the installation is finished you are read yto write your code.

#### Use of The Things Network

You need to create an account with The Things Network and then join or create an application to which you can transmit data. You also need to code your own payload formatter in JavaScript so that the data can be converted into a more readable format, for human users. To find your DevEUI, AppEUI, and AppKey, to enter into the programs, you must go into the 'End devices' section of your application; then you need to click on your device and under the 'Activation information' subheading you should see the DevEUI, AppEUI, and AppKey. Finally create a webhook to Datacake, so that the data can be uplinked and stored in Datacake, to do this go into the 'Integrations' section and click on 'Webhooks'. Once in the webhooks section click 'Add webhook' and select the Datacake template; give the webhhok a name and use the API token from Datacake, found in the API section of the 'Edit Profile' setting. After creating the webhook, you need to go to Datacake and copy the link, found in the LoRaWAN Setup Instructions, into the Uplink message box in the webhook settings.

Screenshots of The Things Network:

Finding the DevEUI, AppEUI, and AppKey:

![Screenshot 2022-08-01 125309](https://user-images.githubusercontent.com/109732245/182142308-c74bb26b-213c-4e1e-8822-56fa0e10aa10.png)

![Screenshot 2022-08-01 105611](https://user-images.githubusercontent.com/109732245/182123652-d956e4b8-fbfd-4d87-8268-1736bf962005.png)

Example Payload Formatter:

![Screenshot 2022-08-01 125406](https://user-images.githubusercontent.com/109732245/182142384-03aabca8-74df-45dd-8115-1297b109103d.png)

![Screenshot 2022-08-01 105833](https://user-images.githubusercontent.com/109732245/182123975-8e80b21a-268b-4a50-9dc2-61327d6acdfb.png)

Where to Find the Uplink Message Link on Datacake:

![Screenshot 2022-08-01 112510](https://user-images.githubusercontent.com/109732245/182128801-4c27dcf1-7d50-4db8-917f-01eae9bc8058.png)

![Screenshot 2022-08-01 111444](https://user-images.githubusercontent.com/109732245/182127271-b5bc7ade-e82e-482e-9939-9554960cc151.png)

#### Use of Datacake

You will have to create an account with Datacake and join the Blenheim workspace. In your account you will need to create a device and in the configuration you will have to create another, similar, payload formatter on Datacake and finally create fields for your data to be stored in. On Datacake you can create a dashboard, so that you can display your data.

Screenshots of Datacake:

Dashboard:

![Screenshot 2022-08-01 125645](https://user-images.githubusercontent.com/109732245/182142823-bc108f2f-8aca-4706-bdbb-b47e390ffe5a.png)

![Screenshot 2022-08-01 131335](https://user-images.githubusercontent.com/109732245/182145325-2e3e3238-425d-40cf-af90-19a1e3196964.png)

Payload Decoder/Formatter:

![Screenshot 2022-08-01 125515](https://user-images.githubusercontent.com/109732245/182142653-b83fe5e6-5db1-451c-be9f-29fd393f97d4.png)

![Screenshot 2022-08-01 112804](https://user-images.githubusercontent.com/109732245/182129130-87980809-1667-4630-9c97-3ca626f27717.png)

#### Light Dependant Resistor (LDR)/Photo-Resistor Process

##### Components Required

- Raspberry Pi Pico with USB Connection to PC
- Breadboard
- RAK4270 with Antenna
- Light Depenedant Resistor (LDR) / Photo-Resistor
- 10 kiloohm Resistor
- 2 M-M Cables
- 4 F-M Cables

The initial use of the RAK module to transmit data from sensors could be with an LDR measuring the surrounding light levels. You need to apply an ADC to the readings from the LDR and convert this value to a percentage, for easier handling. Then use a while loop to constantly check the value of the LDR, and use an if statement to check if it goes below 20%. If this condition is met the data will be transmitted to The Things Network and uplinked to Datacake. The uses of a program such as this could be automating lights turning on or off if a certain light level is reached; this may help save energy because it would prevent lights being left on when they are not needed.

#### Ultrasonic Sensor Process

##### Components Required

- Raspberry Pi Pico with USB Connection to PC
- Breadboard
- RAK4270 with Antenna
- Ultrasonic Sensor (HC-SR04)
- 4 M-M cables
- 8 F-M Cables

Having used the LDR you may wish to move onto using an ultrasonic sensor, in a similar fashion to how you used the LDR. You need to create an algorithm to convert the time taken, for the sound to be emitted from the sensor and reflect back off of an object, into a distance - in centimeters - by using the speed of sound in air and this time in the equation: distance = speed x time. Using this algorithm you are able to check whether an object was closer to the sensor than a set distance, for example 15cm, and transmit the value of the distance to The Things Network and Datacake. Uses of this system involve: water level detection and detecting if people are too close to historic artifacts.

#### Temperature Sensor Process

##### Components Required

- Raspberry Pi Pico with USB Connection to PC
- Breadboard
- RAK4270 with Antenna
- Temperature Sensor
- 6 Jumper Cables
- 4 F-M Cables

Another sensor you may wish to use could be a temperature sensor, to use this with the Raspberry Pi Pico you need to use the analogue output of the sensor. With this value you can calculate the reference voltage, by dividing the analogue output by 65535 (the maximum ADC value) then multiplying this by the input voltage (3.3V). Using the reference voltage you can find the resistance of the thermistor, through the formula 1 / ({(Input Voltage / reference Voltage) - 1} x {1 / Series Resistance}). You can then use this resistance value in the Steinhart equation by doing the following operations: temperature = resistance / 10000; math.log(temperature); temperature + (1 / (25 + 273.15); 1 / temperature; temperature - 273.15. This gives the temperature in °C

#### Particulate Matter Sensor Process

##### Components Required

- Raspberry Pi Pico with USB Connection to PC
- Breadboard
- RAK4270 with Antenna
- Particulate Matter Sensor (PMS5003) and Breakout Board
- 8 F-M Cables

Using the knowledge you have acquired from all of the previous sensors and programs you will be able to connect a particulate matter sensor (PMS) to the raspberry Pi Pico and RAK module and constantly monitor the surrounding air and transmit this data every minute. You will have to install two modules, being: pms5003-micropython and micropython-uasyncio, the implementation of these modules allow you to read the data from the PMS and then transmit this data to The Things Network and Datacake. This has uses within many settings, such as offices, classrooms, and homes because it allows users to see if the air surrounding them is safe which means health risks are minimised.
