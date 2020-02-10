# Write your code here :-)
from microbit import *
import random

heads = 0
tails = 0

while True:
    if accelerometer.was_gesture("shake"):
        for flipcounter in range(1, 11):
            num = random.randint(1, 2)
            # consider 1 a head and 2 a tail
            if (num == 1):
                # head
                display.show("H")
                heads += 1
            else:
                display.show("T")
                tails += 1
            sleep(1000)
        display.scroll(str(heads)+" H "+str(tails)+"T")
        heads = 0
        tails = 0

