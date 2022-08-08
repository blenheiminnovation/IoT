#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created by Joe Lucas
# Blenheim Innovation Team
# Open Sensor Network
# Created Date: 19/07/22
# Version = '1.0'
# ----------------------------------------------------------------------------
"""LEDJoystickControl.py: This program uses an LED, Joystick, and a Raspbery Pi Pico to change the brightness of the LED to the X value of the joystick, it served as an introduction to programming with the Raspberry Pi Pico"""
# ----------------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------------
from machine import Pin, PWM, ADC
import time

led = Pin(15, Pin.OUT)
xAxis = ADC(
    Pin(27)
)  # locates the X pin of the joystick and applies an analogue to digital converter to the value
yAxis = ADC(
    Pin(26)
)  # locates the Y pin of the joystick and applies an analogue to digital converter to the value
pwm = PWM(Pin(15))

pwm.freq(
    1000
)  # Sets the frequency for how often power is switched on and off for the LED

button = Pin(16, Pin.IN, Pin.PULL_UP)

while True:
    xValue = xAxis.read_u16()
    pwm.duty_u16(
        xValue
    )  # Sets the brightness of the LED to the X value of the joystick

timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)
