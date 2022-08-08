#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created by Joe Lucas
# Blenheim Innovation Team
# Open Sensor Network
# Created Date: 19/07/22
# Version = '1.0'
# ----------------------------------------------------------------------------
"""UltrasonicSensor.py: This program uses an Ultrasonic Sensor (US) and a Raspbery Pi Pico to read data from the US and output said data, it served as an introduction to using a US to gain data about the surroundings"""
# ----------------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------------
from machine import Pin
import utime

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

    print("The distance from object is ", distance, "cm")


while True:  # Constantly reads and outputs the data from the US every second
    ultra()
    utime.sleep(1)
