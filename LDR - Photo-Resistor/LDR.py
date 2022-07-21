#!/usr/bin/env python
#-*- coding: utf-8 -*-
#----------------------------------------------------------------------------
#Created by Joe Lucas
#Blenheim Innovation Team
#Open Sensor Network
#Created Date: 19/07/22
#Version = '1.0'
#----------------------------------------------------------------------------
"""LDR.py: This program uses an LDR/Photo-Resistor and a Raspbery Pi Pico to read data from the LDR and output said data, it served as an introduction to using an LDR to gain data about the surroundings"""
#----------------------------------------------------------------------------
#Imports
#----------------------------------------------------------------------------
from machine import ADC, Pin
from time import sleep

photoPIN = 26 #Gets the pin number for the LDR/Photo-Resistor

def readLight(photoGP):
    photores = ADC(Pin(26)) #Reads an analogue value from the LDR
    light = photores.read_u16() #The light value is read using a 16-bit reading function
    light = round(light/65535*100,2) #As the value is a 16-bit reading it ranges between 0-65,535, it is then converted into a percentage for easier handling
    return light

while True: #Reads and outputs the value from the LDR every second
    print('Light: ' + str(readLight(photoPIN)) + '%')
    sleep(1) 