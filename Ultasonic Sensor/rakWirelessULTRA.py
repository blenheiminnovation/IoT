#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created by David Green and Joe Lucas
# Blenheim Innovation Team
# Open Sensor Network
# Created Date: 19/07/22
# Version = '1.0'
# ----------------------------------------------------------------------------
"""rakWirelessULTRA.py: This program uses an Ultrasonic Sensor (US), Raspbery Pi Pico, and RAK4270H to read and transmit data, from the US, to The Things Network and Datacake"""
# ----------------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------------
from machine import UART, ADC, Pin
import time
import utime
import struct
from binascii import hexlify

####

DevEUI = ""  # Insert your DEVEUI here
AppEUI = ""  # Insert your APPEUI here
AppKey = ""  # Insert your APPKEY here
decoded_data = ""
led = Pin(
    25, Pin.OUT
)  # Connects to the onboard LED to give a physical signal of when data is being transmitted
led.value(0)
trigger = Pin(3, Pin.OUT)  # Getting the Ultrasonic sensor's trigger pin
echo = Pin(2, Pin.IN)  # Getting the Ultrasonic sensor's echo pin


def ultra():
    trigger.low()  # Sets the triiger pin to low, to ensure it is not active
    utime.sleep_us(2)
    trigger.high()  # Pulses the trigger pin high for 5 microseconds
    utime.sleep_us(5)
    trigger.low()

    # Check to see if an echo pulse is recieved
    while echo.value() == 0:
        signaloff = (
            utime.ticks_us()
        )  # If no echo pulse isn't recieved, signaloff is updated to contain a timestamp in microseconds

    while echo.value() == 1:
        signalon = (
            utime.ticks_us()
        )  # If an echo pulse is recieved, signalon is updated to store the current timestamp in microseconds

    timepassed = (
        signalon - signaloff
    )  # Stores the total time taken for the pulse to echo back off of the object
    distance = (
        timepassed * 0.0343
    ) / 2  # Converts the time passed into distance, using the speed of sound (343.2ms/1 or 0.0343cm/microsecond)
    return distance


def hexConvert(string):
    encoded = string.encode()
    hexValue = hexlify(string).decode()
    print(hexValue)
    return hexValue


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

## TRY TO JOIN THE NETWORK!##
def joinNetwork():
    decoded_data = ""
    uart.write("at+join\r\n")
    print("joining...")
    while decoded_data != "OK Join Success\r\n":
        try:
            data = uart.read()
            if data:
                decoded_data = data.decode("utf-8")
                if decoded_data == "OK Join Success\r\n":
                    print(decoded_data)
                    time.sleep(5)
                if decoded_data == "ERROR: 99\r\n":
                    raise Exception("Join Error")

                while 1:
                    distance = round(
                        ultra(), 2
                    )  # Constantly checks the distance of the nearest object to the sensor
                    if (
                        distance <= 15.00
                    ):  # If the object becomes closer than 15cm, the distance value is transmitted
                        led.value(1)
                        distanceString = (
                            "US~~Testing~~" + str(distance) + "~~" + " " + "~~" + " "
                        )  # Only one value is outputted by the sensor so the Value 2 and Value 3 fields are left blank
                        payload = hexConvert(distanceString)
                        # testpack = ustruct.pack('h',payload)
                        uart.write("at+send=lora:2:" + payload + "\r\n")
                        led.value(0)
                        time.sleep(
                            60
                        )  # Stops the data from being constantly transmitted, by forcing it to wait for a minute before iterating through the loop again
        except:
            time.sleep(5)
            joinNetwork()


print("join success!")
