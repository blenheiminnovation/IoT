#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created by David Green and Joe Lucas
# Blenheim Innovation Team
# Open Sensor Network
# Created Date: 19/07/22
# Version = '1.0'
# ----------------------------------------------------------------------------
"""rakWirelessLDR.py: This program uses an LDR/Photo-Resitor, Raspbery Pi Pico, and RAK4270H to read and transmit data, from the LDR, to The Things Network and Datacake"""
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
led1 = Pin(27, Pin.OUT)
led2 = Pin(26, Pin.OUT)
led3 = Pin(22, Pin.OUT)
led4 = Pin(21, Pin.OUT)
led5 = Pin(20, Pin.OUT)
led6 = Pin(19, Pin.OUT)
led7 = Pin(18, Pin.OUT)
led8 = Pin(17, Pin.OUT)
photoPIN = 26  # Gets the pin number for the LDR/Photo-Resistor


def readLight(photoGP):
    photores = ADC(Pin(photoGP))  # Reads an analogue value from the LDR
    light = (
        photores.read_u16()
    )  # The light value is read using a 16-bit reading function
    light = round(
        light / 65535 * 100, 2
    )  # As the value is a 16-bit reading it ranges between 0-65,535, it is then converted into a percentage for easier handling
    return light


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
uart.write("AT+NJM=1\r\n")
decoded_data = ""
print("set to OTAA")
while decoded_data != "OK\r\n":
    data = uart.read()
    if data:
        decoded_data = data.decode("utf-8")
        print("OTAA done!\r\n" + decoded_data)

decoded_data = ""
uart.write("AT+CLASS=A\r\n")
print("set to Class A")
while decoded_data != "OK\r\n":
    data = uart.read()
    if data:
        decoded_data = data.decode("utf-8")
        print("Class A done!\r\n" + decoded_data)

decoded_data = ""
uart.write("AT+BAND=4\r\n")
print("set to EU868 region")
while decoded_data != "OK\r\n":
    data = uart.read()
    if data:
        decoded_data = data.decode("utf-8")
        print("EU868 done!\r\n" + decoded_data)

decoded_data = ""
uart.write("AT+DEVEUI=" + DevEUI + "\r\n")
print("set to DEVEUI")
while decoded_data != "OK\r\n":
    data = uart.read()
    if data:
        decoded_data = data.decode("utf-8")
        print("DEVUI done!\r\n" + decoded_data)

decoded_data = ""
uart.write("AT+APPEUI=" + AppEUI + "\r\n")
print("set to APPEUI")
while decoded_data != "OK\r\n":
    data = uart.read()
    if data:
        decoded_data = data.decode("utf-8")
        print("APPEUI done!\r\n" + decoded_data)

decoded_data = ""
uart.write("AT+APPKEY=" + AppKey + "\r\n")
print("set to APPKEY")
while decoded_data != "OK\r\n":
    data = uart.read()
    if data:
        decoded_data = data.decode("utf-8")
        print("APPKEY done!\r\n" + decoded_data)
## END OF SETTING UP ##

## TRY TO JOIN THE NETWORK!##
join_count = 1
def joinNetwork(join_count):
    decoded_data = ""
    uart.write("AT+JOIN=1:0:38:0\r\n")
    print(str(join_count) + " joining...")
    binNum = findBinary(join_count)
    led1.value(int(binNum[0]))
    led2.value(int(binNum[1]))
    led3.value(int(binNum[2]))
    led4.value(int(binNum[3]))
    led5.value(int(binNum[4]))
    led6.value(int(binNum[5]))
    led7.value(int(binNum[6]))
    led8.value(int(binNum[7]))
    time.sleep(10)
    while decoded_data != "OK\r\n":
        try:
            data = uart.read()
            if data:
                decoded_data = data.decode("utf-8")
                print(decoded_data)
                if decoded_data == "OK\r\n":
                    print(decoded_data)
                elif "AT_BUSY_ERROR" in decoded_data:
                    raise Exception("Join Error")

                while 1:
                    brightness = readLight(
                        photoPIN
                    )  # Constantly reads the value from the sensor
                    if (
                        brightness <= 20.00
                    ):  # If the sensor value drops below 20%, the %age value is trasnmitted
                        led.value(1)
                        brightnessString = (
                            "LDR~~TST~~" + str(brightness) + "~~0~~0"
                        )  # Only one value is outputted by the sensor so the Value 2 and Value 3 fields are left blank
                        payload = hexConvert(brightnessString)
                        # testpack = ustruct.pack('h',payload)
                        uart.write("at+send=lora:2:" + payload + "\r\n")
                        led.value(0)
                        time.sleep(
                            15 * 60
                        )  # Stops the data from being constantly transmitted, by forcing it to wait for 15 minutes before iterating through the loop again
        except:
            time.sleep(5)
            joinNetwork()


joinNetwork()
print("join success!")
