# IoT

## Contents

- [IoT](#iot)
  - [Contents](#contents)
  - [Software Used](#software-used)
  - [Programming Process](#programming-process)
    - [Overarching Themes](#overarching-themes)
    - [Setting up Thonny](#setting-up-thonny)
    - [LED Process](#led-process)
      - [Components Required](#components-required)
    - [Light Dependant Resistor (LDR)/Photo-Resistor Process](#light-dependant-resistor-ldrphoto-resistor-process)
      - [Components Required](#components-required-1)
    - [Ultrasonic Sensor Process](#ultrasonic-sensor-process)
      - [Components Required](#components-required-2)
    - [Temperature Sensor Process](#temperature-sensor-process)
      - [Components Required](#components-required-3)
    - [Temperature, Humidity and Pressure Sensor](#temperature-humidity-and-pressure-sensor-process)
      - [Components Required](#components-required-4)
    - [Particulate Matter Sensor Process](#particulate-matter-sensor-process)
      - [Components Required](#components-required-5)
    - [Gas Sensor Process](#gas-sensor-process)
      - [Components Required](#components-required-6)
    - [LoRa Transmission, via the LoRaWAN module (RAK3172 or ASR6501)](#lora-transmission-via-the-lorawan-module-rak3172-or-asr6501)
      - [Setting up the LoRaWAN Module](#setting-up-the-lorawan-module)
      - [Use of The Things Network](#use-of-the-things-network)
      - [Use of Datacake](#use-of-datacake)

## Software Used

- Chrome
- GitHub
- [Thonny](https://thonny.org/)
- [The Things Network](https://www.thethingsnetwork.org/)
- [Datacake](https://app.datacake.de/)
- [Cirkit Designer](https://www.cirkitstudio.com/)

## Programming Process

### Overarching Themes

For all of the following programs you will need the following modules:

- machine
- time
- utime
- struct
- binascii - to convert strings into hexadecimal

### Setting up Thonny

Firstly you will need to download the Thonny IDE, in order to be able to write code for the Raspberry Pi Pico to execute. Once you have succesfully downloaded and installed Thonny, plug your Raspberry Pi Pico into the computer.  (If the Pico does not already have Micropython installed, it will open an explorer window; in that case, remove and reconnect the cable whilst holding the BOOTSEL button - and press the Stop/Restart button at the top of the Thonny window; a window should pop up allowing you to install MicroPython firmware to the Raspberry Pi Pico. Make sure the target device is correct and press install, once the installation is finished you are ready to write your code.)

### LED Process

#### Components Required

- Raspberry Pi Pico with USB Connection to PC
- Breadboard
- LED
- Analogue Joystick
- 220 ohm Resistor
- 5 M-M Cables
- 5 F-M Cables

To begin with you could start with a very basic circuit containing the Raspberry Pi Pico, LED, and 220 ohm resistor all plugged into the breadboard. You should then write the code to blink the LED on and off. Following this you can develop both the circuit and code further by adding in a button, which is then used as a condition in a selection statement with the code to toggle the LED nested in it. Further advancements are made by implementing the ability for the LED to change its brightness, via the use of pulse-width modulation (PWM). Finally you could replace the button with an analogue joystick and use this to change the brightness of the LED based upon the X value of the joystick after an analogue to digital converter (ADC) had been applied to it.

### Light Dependant Resistor (LDR)/Photo-Resistor Process

#### Components Required

- Raspberry Pi Pico with USB Connection to PC
- Breadboard
- Light Dependant Resistor (LDR) / Photo-Resistor
- 10 kiloohm Resistor
- 2 M-M Cables
- 4 F-M Cables

Moving onto using sensors, you could start with an LDR measuring the surrounding light levels. You need to apply an analogue to digital converter (ADC) to the readings from the LDR and convert this value into a percentage, for easier handling. Then use a while loop to constantly check the value of the LDR, and use an if statement to check if it goes below 20%. If this condition is met you could output the data using a print statement. The uses of a program such as this could be automating lights turning on or off if a certain light level is reached; this may help save energy because it would prevent lights being left on when they are not needed.

### Ultrasonic Sensor Process

#### Components Required

- Raspberry Pi Pico with USB Connection to PC
- Breadboard
- Ultrasonic Sensor (HC-SR04)
- 4 M-M cables
- 8 F-M Cables

Having used the LDR you may wish to move onto using an ultrasonic sensor, in a similar fashion to how you used the LDR. You need to create an algorithm to convert the time taken, for the sound to be emitted from the sensor and reflect back off of an object, into a distance - in centimeters - by using the speed of sound in air and this time in the equation:

$$ distance = speed * time $$

Using this algorithm you are able to check whether an object is closer to the sensor than a set distance, for example 15cm, and output the value if the condition is met. Uses of this system involve: water level detection and detecting if people are too close to historic artifacts.

### Temperature Sensor Process

#### Components Required

- Raspberry Pi Pico with USB Connection to PC
- Breadboard
- Temperature Sensor
- 6 M-M Cables
- 4 F-M Cables

Another sensor you may wish to use could be a temperature sensor, to use this with the Raspberry Pi Pico you need to use the analogue output of the sensor. With this value you can calculate the reference voltage, by using the: input voltage (3.3V)(Vi), and the analogue output (AO) in the formula:

$$ Vr = Vi * (AO / 65523) $$

With the reference voltage, series resistance (44900)(Rs), and input voltage (Vi) you can find the resistance of the thermistor (Rt), using the formula:

$$ Rt = 1 / (((Vi / Vr) - 1) * (1 / Rs)) $$

You can then use this resistance (Rt) value in the Steinhart equation, to give the temperature in °C:

$$ (1 / ((log(Rt / 10000)) + (1 / (25 + 273.15))) - 273.12 $$

### Temperature and Humidity Sensor Process

#### Components Required

- Raspberry Pi Pico with USB Connection to PC
- Breadboard
- Temperature and Humidity sensor (DHT22 or DHT11)
- 3 M-M Cables
  
An alternative to the prior sensor is the DHT22 or DHT11 temperature and humidity sensor. This requires use of an additional python library (dht), which should be included in the standard Micropython installation.  These sensors are very similar - the DHT11 reports integers, while the DHT22 reports floating point numbers.

### Temperature, Humidity and Pressure Sensor

#### Components Required

- Raspberry Pi Pico with USB Connection to PC
- Breadboard
- Temperature and Humidity sensor (M5 ENVIII)
- Grove to M Cable
  
Yet another option for temperature and humidity is the M5 ENVIII module.  This has two internal sensors: SHT30 which measures temperature and humidity, and qmp6988 which measures temperature and atmospheric pressure. To use these you will need the appropriate libraries (sht30.py and qmp6988.py), which can be downloaded from https://github.com/cdrajb/M5_ENVIII where you will also find a simple program to print the readings.

### Particulate Matter Sensor Process

#### Components Required

- Raspberry Pi Pico with USB Connection to PC
- Breadboard
- Particulate Matter Sensor (PMS5003) and Breakout Board
- 8 F-M Cables

Using the knowledge you have acquired from all of the previous sensors and programs you will be able to connect a particulate matter sensor (PMS) to the Raspberry Pi Pico and constantly monitor the surrounding air and read this data every minute. You will have to install two modules, being: pms5003-micropython and micropython-uasyncio, the implementation of these modules allow you to read the data from the PMS and then use the values throughout your program. This has uses within many settings, such as offices, classrooms, and homes because it allows users to see if the air surrounding them is safe which means health risks are minimised.

### Gas Sensor Process

#### Components Required

- The Things Uno with USB Connection to PC
- Grove Multichannel Gas Sensor
- 4 pin grove to male jumper cable

Using the Arduino IDE you wil need to download the 'Grove - Multichannel Gas Sensor' library, by going into tools > manage libraries and searching for the name. With the module installed you can get the code to read the sensor value by going into the file tab, clicking on examples then the installed library and then ReadSensorValue_Grove. When you have this code and the Arduino plugged in press the upload button on the top bar of the IDE and then the open serial button in the top right corner. You should now see the values from the sesnor being outputted, you will notice there are more than just NO2 however the others can be deleted if you will not be using them. To be implement the ability to transmit data you need to install another library, TheThingsNetwork, and find the SendOTAA example code. With this code and the NO2 sensor code, you can join the two programs together and use the NO2 value from the sensor to create a payload to be transmitted to The Things Netwok.

### LoRa Transmission, via the LoRaWAN module (RAK3172 or ASR6501)

This project combines the temperature and humidity sensor above with sending the readings out to The Things Network (TTN) using LoRaWAN (Long Range Wide Area Network). You will need an account at TTN to receive and forward the readings - TTN can then forward the readings to DataCake for storage, or send them via MQTT to a client which might store and/or display the readings. 

#### Setting up the LoRaWAN Module

Connect the LoRaWAN Module to the Raspberry Pi Pico and write the code to be able to connect to TTN. You will need to download the pylorawan library from https://github.com/cdrajb/LoRaWAN  Combine this code with the code used for the sensors, to be able to transmit the sensor readings to TTN. You create strings to act as payloads in the format: Sensor Type, Sensor Name, Value 1, Value 2, and Value 3, using the values from the sensor and hardcoding the sensor type and name in the program.  Note that all three Value fields are only required for the particulate matter and temperature and humidity sensors; if you only have a DHT11 for instance, you will only need two of these value fields, so simply set unused values to 0. Then convert the string payload into hexadecimal so that it can be transmitted over LoRaWAN.

#### Use of The Things Network

You need to create an account with The Things Network: click on your profile and select console then join or create an application to which you can transmit data, and create your device in this application. When you create the application, you need to specify the DevEUI (normally this is printed on the device and/or programmed into it by the manufacturer), AppEUI (also known as JoinEUI; this may be provided by the manufacturer or you can provide it - if you provide it you can use all zeros if you wish).  Once you've entered those, you need to generate an Appkey (which you then program into the device using your program).  
When the device tries to join the network, if the DevEUI, AppEUI and Appkey configured in TTN match the ones in the application, they will link up and you will see the sent data in the TTN application.   To enter your DevEUI, AppEUI, and generate your AppKey, go to the 'End devices' section of your application in TTN; then click on "Add device"

You can also code your own payload formatter in JavaScript and add this to TTN so that the data can be converted into a more readable format for human users (see below for more on this)  

After this you can then test your program which uses the LoRaWAN module, checking for a connection to The Things Network and then the transmission of data. 
In TTN, you should see received data: open the application end device, select "Live data".  Mouse over  { decodedData {...} } to see the data decoded by your payload formatter. 

TTN does not keep a history of your data, so finally you need a way to save or download the data...  
One option is to use a service such as Datacake - this can connect to TTN and save the readings into a database (which you can later query and view the contents)
Or you could use the MQTT server in TTN and run an mqtt client to subscribe to the feed from this server and read the readings, save them into a local database, graph them, etc.

For Datacake, you need to create a webhook in TTN, so that the data can be uplinked and stored in Datacake; to do this go into the 'Integrations' section and click on 'Webhooks'.  Once in the webhooks section click 'Add webhook' and select the Datacake template; give the webhook a name and use the API token from Datacake, found in the API section of the 'Edit Profile' setting.  After creating the webhook, you need to go to Datacake and copy the link, found in the LoRaWAN Setup Instructions, into the Uplink message box in the webhook settings." 

To use MQTT, under Applications in TTN, select your application, then in the left-hand frame select Integrations, MQTT, Generate new API key.  Copy the key (password) and save it, also note the server name and username (you will also receive an email with the key)
If you have installed mosquitto on a client, you can use this to subscribe to the MQTT feed, and view the published data, for example:
mosquitto_sub -h <MQTT-server> -t "#" -u <username> -P <password> -v    (using '#' will subscribe to all the info, so you will see the join requests as well as any data).  Other options might be to use a python script to subscribe and manipulate the data, or an MQTT Dashboard app such as this one for Android: 
https://play.google.com/store/apps/details?id=com.app.vetru.mqttdashboard  

Screenshots of The Things Network:

Finding the DevEUI, AppEUI, and AppKey:

![Screenshot 2022-08-01 125309](https://user-images.githubusercontent.com/109732245/182142308-c74bb26b-213c-4e1e-8822-56fa0e10aa10.png)

![Screenshot 2022-08-01 105611](https://user-images.githubusercontent.com/109732245/182123652-d956e4b8-fbfd-4d87-8268-1736bf962005.png)

Example Payload Decoder/Formatter:

![Screenshot 2022-08-01 125406](https://user-images.githubusercontent.com/109732245/184601598-fd84f3fd-15ea-4c5b-b0f0-860a1c60f2b3.jpg)

![Screenshot 2022-08-01 105833](https://user-images.githubusercontent.com/109732245/182123975-8e80b21a-268b-4a50-9dc2-61327d6acdfb.png)

Where to Find the Uplink Message Link on Datacake:

![Screenshot 2022-08-01 112510](https://user-images.githubusercontent.com/109732245/182128801-4c27dcf1-7d50-4db8-917f-01eae9bc8058.png)

![Screenshot 2022-08-01 111444](https://user-images.githubusercontent.com/109732245/182127271-b5bc7ade-e82e-482e-9939-9554960cc151.png)

#### Use of Datacake

You will have to create an account with Datacake. In your account you will need to create a device, by pressing the 'Add Device' Button and selecting the LoRaWAN option then select 'New Product' and give the product a name; select The Things Stack V3 as the Network Server, after this enter the devices DevEUI and name. Finally select the free plan and add the device. Then in the configuration you will have to create another, similar, payload formatter on Datacake and finally create fields for your data to be stored in. On Datacake you can create a dashboard, so that you can display your data.

Screenshots of Datacake:

Dashboard:

![Screenshot 2022-08-01 125645](https://user-images.githubusercontent.com/109732245/182142823-bc108f2f-8aca-4706-bdbb-b47e390ffe5a.png)

![Screenshot 2022-08-01 131335](https://user-images.githubusercontent.com/109732245/182145325-2e3e3238-425d-40cf-af90-19a1e3196964.png)

Example Payload Decoder/Formatter:

![Screenshot 2022-08-01 125515](https://user-images.githubusercontent.com/109732245/182142653-b83fe5e6-5db1-451c-be9f-29fd393f97d4.png)

![Screenshot 2022-08-01 112804](https://user-images.githubusercontent.com/109732245/182129130-87980809-1667-4630-9c97-3ca626f27717.png)
