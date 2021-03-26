from gpiozero import LED
from time import sleep

led = LED(17)
led2 = LED(27)

while True:
    led.on()
    led2.off()
    sleep(1)
    led.off()
    led2.on()
    sleep(1)
    