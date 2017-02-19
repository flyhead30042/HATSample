from sense_hat import SenseHat
from time import sleep
from datetime import datetime

sense = SenseHat()
green=( 0, 100, 0)
red =(100, 0, 0)


sense.show_message(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
sleep(1)
sense.clear()

t = round(sense.get_temperature(),1)
p = round(sense.get_pressure(),1)
h = round(sense.get_humidity(),1)

if 18.3 < t < 26.7:
    color = green
else:
    color = red

msg = "Tempe = {0}".format(t)
sense.show_message(msg, text_colour=color)
sleep(1)
sense.clear()

if 970 < p < 1027:
    color = green
else:
    color = red

msg = "Pressure = {0}".format(p)
sense.show_message(msg, text_colour=color)
sleep(1)
sense.clear()

if h < 60:
    color = green
else:
    color = red

msg = "Humidity = {0}".format(h)

sense.show_message(msg, text_colour=color)
sleep(1)
sense.clear()




