# Ultrasonic distance sensor example
#  Adapted from https://www.firialabs.com/blogs/lab-notes/ultrasonic-distance-sensor-with-python-and-the-micro-bit

from microbit import *
from machine import time_pulse_us

trig = pin2
echo = pin1

trig.write_digital(0)
echo.read_digital()

while True:
    trig.write_digital(1)
    trig.write_digital(0)
    microsec = time_pulse_us(echo, 1)
    time_echo = microsec / 1000000
    dist_cm = (time_echo / 2) * 34300
    print((dist_cm,))
    # or in inches
    #dist_inches = dist_cm/2.54
    #print((dist_inches,))
    sleep(500)

