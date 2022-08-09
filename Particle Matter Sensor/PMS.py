#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created by Joe Lucas
# Blenheim Innovation Team
# Open Sensor Network
# Created Date: 19/07/22
# Version = '1.0'
# ----------------------------------------------------------------------------
"""PMS.py: This program uses a Particle Matter Sensor (PMS) and a Raspbery Pi Pico to read data from the PMS and output said data, it served as an introduction to using a PMS to gain data about the surroundings"""
# ----------------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------------
import time
from pms5003 import PMS5003
import machine

print(
    """pms5003_test.py - Continously print all data values.
"""
)


# Uses the pms5003 module to set up the sensor, to be able to read the data from it
pms5003 = PMS5003(
    uart=machine.UART(1, tx=machine.Pin(4), rx=machine.Pin(5), baudrate=9600),
    pin_enable=machine.Pin(3),
    pin_reset=machine.Pin(2),
    mode="active",
)


while True:
    data = pms5003.read()
    print(data)  # Outputs all data values from the PMS
    print(data.data[0])  # Outputs the first data value from the PMS
    print(data.data[1])  # Outputs the second data value from the PMS
    print(data.data[2])  # Outputs the third data value from the PMS
    time.sleep(1.0)
