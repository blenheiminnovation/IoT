import machine
import utime
#Setup the onboard LED Pin as an output
LED = machine.Pin("LED",machine.Pin.OUT)
while True:
   LED.on()
   utime.sleep(0.5)
   LED.off()
   utime.sleep(0.5)
