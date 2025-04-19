import machine
import time
led = machine.Pin(2,machine.Pin.OUT)
sw = machine.Pin(0,machine.Pin.IN)
while True: 
    try:
        while sw.value()==0:
            led.on()
    except :
        led.off()
    finally:
        led.off()
        time.sleep(0.5)