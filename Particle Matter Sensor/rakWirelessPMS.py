#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created by David Green and Joe Lucas
# Blenheim Innovation Team
# Open Sensor Network
# Created Date: 19/07/22
# Version = '1.0'
# ----------------------------------------------------------------------------
"""rakWirelessPMS.py: This program uses a Particle Matter Sensor (PMS), Raspbery Pi Pico, and RAK4270H to read and transmit data, from the PMS, to The Things Network and Datacake"""
# ----------------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------------
from machine import UART, ADC, Pin
import time
import utime
import struct
from binascii import hexlify
from pms5003 import PMS5003

####

DevEUI = ""  # Insert your DEVEUI here
AppEUI = ""  # Insert your APPEUI here
AppKey = ""  # Insert your APPKEY here
led1 = Pin(27, Pin.OUT)
led2 = Pin(26, Pin.OUT)
led3 = Pin(22, Pin.OUT)
led4 = Pin(21, Pin.OUT)
led5 = Pin(20, Pin.OUT)
led6 = Pin(19, Pin.OUT)
led7 = Pin(18, Pin.OUT)
led8 = Pin(17, Pin.OUT)
decoded_data = ""
led = Pin(
    25, Pin.OUT
)  # Connects to the onboard LED to give a physical signal of when data is being transmitted
led.value(0)

# Uses the pms5003 module to set up the sensor, to be able to read the data from it
pms5003 = PMS5003(
    uart=machine.UART(1, tx=machine.Pin(4), rx=machine.Pin(5), baudrate=9600),
    pin_enable=machine.Pin(29),
    pin_reset=machine.Pin(2),
    mode="active",
)


def hexConvert(
    string,
):  # Acts to convert the payload into hexadecimal format, so that it can be sent to The Things Network and Datacake to be decoded on each of these platforms
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
                    led.value(1)
                    data = pms5003.read()
                    dataArray = data.data[
                        :3
                    ]  # This gets the first 3 values from the sensor data, which are the only values required for this use case
                    print(dataArray[0])
                    print(dataArray[1])
                    print(dataArray[2])
                    distanceString = (
                        "PMS~~TST~~"
                        + str(dataArray[0])
                        + "~~"
                        + str(dataArray[1])
                        + "~~"
                        + str(dataArray[2])
                    )  # This acts as the payload for trasnmission and is in the structure: Sensor Type, Sensor Name, Value 1, Value 2, Value 3
                    payload = hexConvert(distanceString)
                    # testpack = ustruct.pack('h',payload)
                    uart.write(
                        "at+send=lora:2:" + payload + "\r\n"
                    )  # Sends the payload to The Things Network, which then forward uplinks the data to Datacake
                    led.value(0)
                    time.sleep(
                        15 * 60
                    )  # Stops the data from being constantly transmitted, by forcing it to wait for 15 minutes before iterating through the loop again
        except:
            time.sleep(5)
            joinNetwork()


joinNetwork()
print("join success!")
