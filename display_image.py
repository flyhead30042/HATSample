from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
image = []

a = 1
while (a < 4):
    # prepare a image
    for i in range(0, 64, 1):
        r1 = randint(0, 255)
        r2 = randint(0, 255)
        r3 = randint(0, 255)

        pix = [r1, r2, r3]
        # print(pix)
        image.append(pix)

    # show index on hat
    sense.show_letter(str(a))
    sleep(1)
    sense.clear()

    # show image on hat
    sense.set_pixels(image)

    # for next round
    sleep(3)
    sense.clear()
    image.clear()
    a += 1
