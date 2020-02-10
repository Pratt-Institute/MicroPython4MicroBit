# Heartbeat
from microbit import *

# Start with default of one 1 sec between beats
time_between_beats = 1000

while True:
    if (button_a.is_pressed() or accelerometer.was_gesture("shake")):
        if (time_between_beats > 100):
            time_between_beats -= 100
        display.show(Image.HEART, clear=True)
        sleep(time_between_beats)
    elif (button_b.is_pressed()):
        time_between_beats += 100
        display.show(Image.HEART, clear=True)
        sleep(time_between_beats)
    else:
        display.show(Image.HEART, clear=True)
        sleep(time_between_beats)