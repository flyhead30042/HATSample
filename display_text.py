

from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

s = "Hello , my name is CI, nice to meet you"

list = s.split(" ")

for w in list:
    r1 = randint(0, 255)
    r2 = randint(0, 255)
    r3 = randint(0, 255)
    sense.show_message(w, text_colour=[r1, r2, r3])
    sleep(0.6)

sense.show_letter("!",text_colour=[0, 0, 0], back_colour=[255, 255, 255])
sleep(1)
sense.clear()
