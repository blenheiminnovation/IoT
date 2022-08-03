from machine import Pin, ADC
import math
import time

tempPin = ADC(Pin(26, Pin.IN))

while 1:
    ADCValue = tempPin.read_u16()  # Reading the value in 16bits unsigned
    print(tempPin.read_u16())
    V0 = (
        ADCValue / 65535
    ) * 3.3  # Calculating the reference voltage, using the ratio between the measured value and the maximum ADC value. The multiplying the input voltage by this ratio
    print(V0)

    resistance = ((3.3 / V0) - 1) * (
        1 / 44900
    )  # Using the input and reference voltage, as well as the series resistance
    resistance = 1 / resistance
    print(resistance)

    steinhart = (
        resistance / 10000
    )  # Using the calculated, series and nominal values in the Steinhart equation to find the temperature in Kelvin
    print(steinhart)
    steinhart = math.log(steinhart)
    print(steinhart)
    steinhart /= 3950
    print(steinhart)
    steinhart += 1 / (25 + 273.15)
    print(steinhart)
    steinhart = 1 / steinhart
    print(steinhart)
    steinhart -= 273.15  # Converting from Kelvin into Centigrade
    print(steinhart)
    print(steinhart)
    time.sleep(10)
