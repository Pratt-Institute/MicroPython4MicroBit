from microbit import *

while True:
    if pin0.is_touched():
        display.show(Image.SURPRISED)
        sleep(2000)
    else:
        display.show(Image.ASLEEP)

