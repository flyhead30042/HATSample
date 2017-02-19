from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()

green = (0, 100, 0)
red = (100, 0, 0)
white = (255, 255, 255)


def is_moving(a, b):
    n = abs(a - b)
    if n > 0.06:
        print("{0}-{1} = {2}".format(a, b, n))
        return True
    else:
        return False


while True:
    acceleration = sense.get_accelerometer_raw()

    x1 = round(acceleration['x'], 5)
    y1 = round(acceleration['y'], 5)
    z1 = round(acceleration['x'], 5)

    sleep(0.1)

    acceleration = sense.get_accelerometer_raw()
    x2 = round(acceleration['x'], 5)
    y2 = round(acceleration['y'], 5)
    z2 = round(acceleration['x'], 5)

    if is_moving(x1, x2):
        sense.show_message("!!!", text_colour=white, back_colour=red)
    else:
        sense.clear()
