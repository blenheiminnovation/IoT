from machine import Pin, UART
import time
import pylorawan 
import creds_config
import dht
from binascii import hexlify

# Tested with a Raspberry PI Pico and M5 LoRaWAN868
def hexConvert(
    string,
):  # Acts to convert the payload into hexadecimal format, so that it can be sent to The Things Network and Datacake to be decoded on each of these platforms
    encoded = string.encode()
    hexValue = hexlify(string).decode()
    print(hexValue)
    return hexValue

sensor = dht.DHT11(Pin(2))

# Talk to the modem using the UART0 TRansmitter(Tx) / Receiver(Rx)
#uart = UART(1, 9600)  # use RPI PICO
uart = UART(1, 115200, tx=Pin(4), rx=Pin(5))  # use RPI PICO; pins 4,5 are UART1 
# The device uses AT commands like a traditional modem, so i'll refer to it as a modem.
#
modem = pylorawan.LorawanModem(uart, "ASR6501", debug=False)
# Configure it to use OTAA (rather ABP comms) using keys from the device itself and The Things Network Console
# dev_eui is printed in the top of the chip casing
#
print("configuring OTAA...")
modem.configure_otaa(region="EU868",
                     dev_eui=creds_config.dev_eui_asr6501,
                     app_eui=creds_config.app_eui,
                     app_key=creds_config.app_key,
                     lora_class="A")
print("configured OTAA.  Joining...")
# Try and join the network (often takes a few tries, it will automatically retry 8 times)
if modem.join():
    print("joined, sending...")
    # It worked...
    # Send some made up hex data to the TTN server on port 1 to clear out the send buffers
    # Note that the first reading at TTN will be old data but the correct reading will follow immediately
    modem.send_data("AABBCCDD")

    while 1:
                    now=time.localtime()
                    tmstmp = time.time()
                    print("Time: {}:{}:{}".format(now[3], now[4], now[5]))
                    sensor.measure()
                    temperature = sensor.temperature()
                    humidity = sensor.humidity()
                    valuesString = (
                        "TMP~~TST~~" + str(tmstmp) + "~~" + str(temperature) + "~~" + str(humidity) +"~~0"
                    )  # This acts as the payload for transmission and is in the structure: Sensor Type, Sensor Name, timestamp, Value 1, Value 2, Value 3
                    print(valuesString)
                    payload = hexConvert(valuesString)
                    modem.send_data(payload,2,1) # data,port,tries
                    #uart.write(
                    #    "AT+SEND=2:" + payload + "\r\n"
                    #)  # Sends the payload to The Things Network, which then forward uplinks the data to Datacake
                    time.sleep(
                        5 * 60
                    )  # Stops the data from being constantly transmitted, by forcing it to wait for 15 minutes before iterating through the loop again
else:
    # Could not join the network...
        print("Failed to Join, are your keys correct? Is there a gateway in range?")
  
