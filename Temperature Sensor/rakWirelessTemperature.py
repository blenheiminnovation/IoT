#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created by David Green and Joe Lucas
# Blenheim Innovation Team
# Open Sensor Network
# Created Date: 19/07/22
# Version = '1.0'
# ----------------------------------------------------------------------------
"""rakWirelessTemperature.py: This program uses a Temperature Sensor (TS) (NTC-MF52 3950
), Raspbery Pi Pico, and RAK4270H to read and transmit data, from the TS, to The Things Network and Datacake"""
# ----------------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------------
from machine import UART, ADC, Pin
import time
import utime
import struct
import math
from binascii import hexlify

####

DevEUI = ""  # Insert your DEVEUI here
AppEUI = ""  # Insert your APPEUI here
AppKey = ""  # Insert your APPKEY here
decoded_data = ""
led = Pin(
    15, Pin.OUT
)  # Connects to the onboard LED to give a physical signal of when data is being transmitted
tempPin = ADC(Pin(26, Pin.IN))
led.value(0)


def hexConvert(
    string,
):  # Acts to convert the payload into hexadecimal format, so that it can be sent to The Things Network and Datacake to be decoded on each of these platforms
    encoded = string.encode()
    hexValue = hexlify(string).decode()
    print(hexValue)
    return hexValue


def findTemp(ADCValue):
    V0 = (
        ADCValue / 65535
    ) * 3.3  # Calculating the reference voltage, using the ratio between the measured value and the maximum ADC value. Then multiplying the input voltage by this ratio

    resistance = ((3.3 / V0) - 1) * (
        1 / 44900
    )  # Using the input and reference voltage, as well as the series resistance
    resistance = 1 / resistance

    temperature = (
        resistance / 10000
    )  # Using the calculated, series and nominal values in the Steinhart equation to find the temperature in Kelvin
    temperature = math.log(temperature)
    temperature /= 3950
    temperature += 1 / (25 + 273.15)
    temperature = 1 / temperature
    temperature -= 273.15  # Converting from Kelvin into Centigrade
    temperature = round(temperature, 2)

    return temperature


uart = UART(0, 115200)  # use RPI PICO GP0 and GP1

# Use lines below to display the firmware version and config settings
# uart.write('at+version\r\n')
# uart.write('at+get_config=lora:status\r\n')
# data = uart.read()
# if data:
#    decoded_data = data.decode('utf-8')
#    print("Check Config:" + decoded_data)

## Setup the wireless module OTAA, Class, Region, keys##
uart.write("at+set_config=lora:join_mode:0\r\n")
print("set to OTAA")
while decoded_data != "OK\r\n":

    data = uart.read()

    if data:
        decoded_data = data.decode("utf-8")
        print("OTAA done!\r\n" + decoded_data)

decoded_data = ""
uart.write("at+set_config=lora:class:0\r\n")
print("set to Class A")


while decoded_data != "OK\r\n":
    data = uart.read()
    if data:
        decoded_data = data.decode("utf-8")
        print("Class A done!\r\n" + decoded_data)

decoded_data = ""
uart.write("at+set_config=lora:region:EU868\r\n")
print("set to EU868 region")
while decoded_data != "OK\r\n":
    data = uart.read()
    if data:
        decoded_data = data.decode("utf-8")
        print("EU868 done!\r\n" + decoded_data)

decoded_data = ""
uart.write("at+set_config=lora:dev_eui:" + DevEUI + "\r\n")
print("set to DEVEUI")
while decoded_data != "OK\r\n":
    data = uart.read()
    if data:
        decoded_data = data.decode("utf-8")
        print("DEVUI done!\r\n" + decoded_data)

decoded_data = ""
uart.write("at+set_config=lora:app_eui:" + AppEUI + "\r\n")
print("set to APPEUI")
while decoded_data != "OK\r\n":
    data = uart.read()
    if data:
        decoded_data = data.decode("utf-8")
        print("APPEUI done!\r\n" + decoded_data)

decoded_data = ""
uart.write("at+set_config=lora:app_key:" + AppKey + "\r\n")
print("set to APPKEY")
while decoded_data != "OK\r\n":
    data = uart.read()
    if data:
        decoded_data = data.decode("utf-8")
        print("APPKEY done!\r\n" + decoded_data)
## END OF SETTING UP ##

join_count = 1
## TRY TO JOIN THE NETWORK!##
def joinNetwork(join_count):
    decoded_data = ""
    uart.write("at+join\r\n")
    print(str(join_count) + " joining...")
    while decoded_data != "OK Join Success\r\n":
        try:
            data = uart.read()
            if data:
                decoded_data = data.decode("utf-8")
                if decoded_data == "OK Join Success\r\n":
                    print(decoded_data)
                elif decoded_data == "ERROR: 99\r\n":
                    raise Exception("Join Error")

                while 1:
                    led.value(1)
                    ADCValue = (
                        tempPin.read_u16()
                    )  # Reading the value in 16bits unsigned
                    temperature = findTemp(ADCValue)
                    temperatureString = (
                        "TMP~~TST~~" + str(temperature) + "~~0~~0"
                    )  # This acts as the payload for trasnmission and is in the structure: Sensor Type, Sensor Name, Value 1, Value 2, Value 3
                    payload = hexConvert(temperatureString)
                    uart.write(
                        "at+send=lora:2:" + payload + "\r\n"
                    )  # Sends the payload to The Things Network, which then forward uplinks the data to Datacake
                    led.value(0)
                    time.sleep(
                        15 * 60
                    )  # Stops the data from being constantly transmitted, by forcing it to wait for 15 minutes before iterating through the loop again
        except:
            try:
                time.sleep(5)
                joinNetwork(join_count + 1)
            except RuntimeError:
                print("Join Error")
                break


joinNetwork(join_count)
