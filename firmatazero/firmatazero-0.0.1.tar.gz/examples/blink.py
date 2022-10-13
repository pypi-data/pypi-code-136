from time import sleep

from firmatazero import LED

led = LED(13)
while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
