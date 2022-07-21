#!/usr/bin/env python
#-*- coding: utf-8 -*-
#----------------------------------------------------------------------------
#Created by David Green and Joe Lucas
#Blenheim Innovation Team
#Open Sensor Network
#Created Date: 19/07/22
#Version = '1.0'
#----------------------------------------------------------------------------
"""rakWirelessLDR.py: This program uses an LDR/Photo-Resitor, Raspbery Pi Pico, and RAK4270H to read and transmit data, from the LDR, to The Things Network and Datacake"""
#----------------------------------------------------------------------------
#Imports
#----------------------------------------------------------------------------
from machine import UART, ADC, Pin
import time
import utime
import struct
from binascii import hexlify
####

decoded_data = ""
led = Pin(25, Pin.OUT)
led.value(0)
photoPIN = 26 #Gets the pin number for the LDR/Photo-Resistor

def readLight(photoGP):
    photores = ADC(Pin(26)) #Reads an analogue value from the LDR
    light = photores.read_u16() #The light value is read using a 16-bit reading function
    light = round(light/65535*100,2) #As the value is a 16-bit reading it ranges between 0-65,535, it is then converted into a percentage for easier handling
    return light

def hexConvert(string):
    encoded = string.encode()
    hexValue = hexlify(string).decode()
    print(hexValue)
    return hexValue

uart = UART(0, 115200)  # use RPI PICO GP0 and GP1

# Use lines below to display the firmware version and config settings
#uart.write('at+version\r\n')
#uart.write('at+get_config=lora:status\r\n')
#data = uart.read()
#if data:
#    decoded_data = data.decode('utf-8')
#    print("Check Config:" + decoded_data)

## Setup the wireless module OTAA, Class, Region, keys##
uart.write('at+set_config=lora:join_mode:0\r\n')
print("set to OTAA")
while(decoded_data != "OK\r\n"):
    
    data = uart.read()
    
    if data:
        decoded_data = data.decode('utf-8')
        print("OTAA done!\r\n" + decoded_data)
        
decoded_data = ""
uart.write('at+set_config=lora:class:0\r\n')
print("set to Class A")


while(decoded_data != "OK\r\n"):
    data = uart.read()
    if data:
        decoded_data = data.decode('utf-8')
        print("Class A done!\r\n" + decoded_data)

decoded_data = ""
uart.write('at+set_config=lora:region:EU868\r\n')
print("set to EU868 region")
while(decoded_data != "OK\r\n"):
    data = uart.read()
    if data:
        decoded_data = data.decode('utf-8')
        print("EU868 done!\r\n" + decoded_data)

decoded_data = ""
uart.write('at+set_config=lora:dev_eui:60C5A8FFFE78F38E\r\n')
print("set to DEVEUI")
while(decoded_data != "OK\r\n"):
    data = uart.read()
    if data:
        decoded_data = data.decode('utf-8')
        print("DEVUI done!\r\n" + decoded_data)

decoded_data = ""
uart.write('at+set_config=lora:app_eui:1000000000000009\r\n')
print("set to APPEUI")
while(decoded_data != "OK\r\n"):
    data = uart.read()
    if data:
        decoded_data = data.decode('utf-8')
        print("APPEUI done!\r\n" + decoded_data)

decoded_data = ""
uart.write('at+set_config=lora:app_key:170E5E7876C0A42BD9CEB01CE2786544\r\n')
print("set to APPKEY")
while(decoded_data != "OK\r\n"):
    data = uart.read()
    if data:
        decoded_data = data.decode('utf-8')
        print("APPKEY done!\r\n" + decoded_data)
## END OF SETTING UP ##

## TRY TO JOIN THE NETWORK!##
decoded_data = ""
uart.write('at+join\r\n')
print("joining...")
while(decoded_data != "OK Join Success\r\n"):
    data = uart.read()
    if data:
        decoded_data = data.decode('utf-8')
        print(decoded_data)

print("join success!")

while(1):
    brightness = readLight(photoPIN) #Constantly reads the value from the sensor
    if brightness <= 20.00: #If the sensor value drops below 20%, the %age value is trasnmitted
        led.value(1)
        brightnessString = "LDR~~Testing~~" + str(brightness) + "~~" + " " + "~~" + " " #Only one value is outputted by the sensor so the Value 2 and Value 3 fields are left blank
        payload = hexConvert(brightnessString)
        #testpack = ustruct.pack('h',payload)
        uart.write('at+send=lora:2:' + payload + '\r\n')
        led.value(0)
        time.sleep(60) #Stops the data from being constantly transmitted, by forcing it to wait for a minute before iterating through the loop again
