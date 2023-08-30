from machine import Pin, UART
import time
import pylorawan 
import creds_config
import dht
from binascii import hexlify

# Tested with a Raspberry PI Pico and M5 LoRaWAN868
def hexConvert(
    string,
):  # Converts the payload into hexadecimal format so that it can be sent to The Things Network
    encoded = string.encode()
    hexValue = hexlify(string).decode()
    print(hexValue)
    return hexValue

# Tested with a DHT11 temperature and humidity sensor
sensor = dht.DHT11(Pin(2))

# Talk to the modem using the UART0 TRansmitter(Tx) / Receiver(Rx)
uart = UART(1, 115200, tx=Pin(4), rx=Pin(5))  # use RPI PICO; pins 4,5 are UART1 

# The device uses AT commands like a traditional modem, so we'll refer to it as a modem.
modem = pylorawan.LorawanModem(uart, "ASR6501", debug=False)

# Configure it to use OTAA (rather than ABP comms) using keys from the device itself and The Things Network Console
print("configuring OTAA...")
modem.configure_otaa(region="EU868",
                     dev_eui=creds_config.dev_eui_asr6501,
                     app_eui=creds_config.app_eui,
                     app_key=creds_config.app_key,
                     lora_class="A")
print("configured OTAA.  Attempting to join...")

# Try and join the network (often takes a few tries, it will automatically retry 8 times)
if modem.join():
    print("joined, sending...")
    # It worked...
    # Send some made up hex data to the TTN server on port 1 to clear out the send buffers
    # Note that the first reading at TTN will likely be old data but the correct reading should follow immediately
    modem.send_data("AABBCCDD")

# Now start a loop to send readings
    while 1:
                    now=time.localtime()
                    print("Time: {}:{}:{}".format(now[3], now[4], now[5]))
                    sensor.measure()
                    temperature = sensor.temperature()
                    humidity = sensor.humidity()
                    valuesString = (
                        "TMP~~TST~~" + str(temperature) + "~~" + str(humidity) +"~~0"
                    )  # This acts as the payload for transmission and is in the structure: Sensor Type, Sensor Name, Value 1, Value 2, Value 3 (value3 is not used here)
                    print(valuesString)
                    payload = hexConvert(valuesString)
                    modem.send_data(payload,2,1) # data,port,tries
                    # Sends the payload to The Things Network.  TTN may forward the data to Datacake, or you can use mqtt
                    time.sleep(
                        15 * 60
                    )  # Stops the data from being constantly transmitted; waits for 15 minutes before iterating through the loop again
else:
    # Could not join the network...
        print("Failed to Join, are your keys correct? Is there a gateway in range?")
  
