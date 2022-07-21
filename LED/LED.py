#!/usr/bin/env python
#-*- coding: utf-8 -*-
#----------------------------------------------------------------------------
#Created by Joe Lucas
#Blenheim Innovation Team
#Open Sensor Network
#Created Date: 19/07/22
#Version = '1.0'
#----------------------------------------------------------------------------
"""LED.py: This program uses an LED and a Raspbery Pi Pico to turn the LED on and off in an iterative manner, it served as an introduction to programming with the Raspberry Pi Pico"""
#----------------------------------------------------------------------------
#Imports
#----------------------------------------------------------------------------
from machine import Pin, Timer
import time

led = Pin(15, Pin.OUT) #Locates the Pin of the external LED
timer = Timer()

def blink(timer):
    led.toggle() #Inverts the value of the LED
    
timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink) #Sets the timer to be a frequency of 2.5Hz, meaning the LED will toggle 2.5 times per second