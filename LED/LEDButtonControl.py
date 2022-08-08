#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created by Joe Lucas
# Blenheim Innovation Team
# Open Sensor Network
# Created Date: 19/07/22
# Version = '1.0'
# ----------------------------------------------------------------------------
"""LEDButtonControl.py: This program uses an LED, button, and a Raspbery Pi Pico to toggle the LED on and off if the button was pressed, it served as an introduction to programming with the Raspberry Pi Pico"""
# ----------------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------------
from machine import Pin
import time

led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)  # Locates the button and defines it as an input

while True:
    if button.value():  # Switches the value of the LED when the button is held down
        led.toggle()
        time.sleep(0.5)
