from microbit import *

# Flash led with signal wire
# attached to pin0
while True:
    # Turn pin0 on
    pin0.write_digital(1)
    sleep(1000)
    # Turn pin0 off
    pin0.write_digital(0)
    sleep(1000)
