from time import sleep

from firmatazero import Servo

servo = Servo(9)
while True:
    servo.min()
    sleep(1)
    servo.mid()
    sleep(1)
    servo.max()
    sleep(1)
