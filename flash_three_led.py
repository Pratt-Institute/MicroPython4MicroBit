from microbit import *

while True:
    # Turn pin0 on
    pin0.write_digital(1)
    sleep(1000)
    # Turn pin0 off
    pin0.write_digital(0)
    # Turn pin1 on
    pin1.write_digital(1)
    sleep(1000)
    # Turn pin1 off
    pin1.write_digital(0)
    # Turn pin2 on
    pin2.write_digital(1)
    sleep(1000)
    # Turn pin0 off
    pin2.write_digital(0)
