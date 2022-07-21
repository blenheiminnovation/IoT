#!/usr/bin/env python
#-*- coding: utf-8 -*-
#----------------------------------------------------------------------------
#Created by Joe Lucas
#Blenheim Innovation Team
#Open Sensor Network
#Created Date: 19/07/22
#Version = '1.0'
#----------------------------------------------------------------------------
"""LEDBrightness.py: This program uses an LED and a Raspbery Pi Pico to gradually increase and then decrease the brightness of the LED, it served as an introduction to programming with the Raspberry Pi Pico"""
#----------------------------------------------------------------------------
#Imports
#----------------------------------------------------------------------------
from machine import Pin, PWM
from time import sleep
led = Pin(15, Pin.OUT)
pwm = PWM(Pin(15))

pwm.freq(1000) #Sets the frequency for how often power is switched on and off for the LED

while True:
    for duty in range(65025): #Increases the brightness of the LED
        pwm.duty_u16(duty)
        sleep(0.0001)
    for duty in range(65025, 0, -1): #Decreases the brightness of the LED
        pwm.duty_u16(duty)
        sleep(0.0001)