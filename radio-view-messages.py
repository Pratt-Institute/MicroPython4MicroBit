# Simple radio example
# Adapted from https://microbit-micropython.readthedocs.io/en/latest/radio.html
import radio
from microbit import *

# The radio won't work unless it's switched on.
radio.on()

# Event loop.
while True:
    details = radio.receive_full()
    if details:
        msg, rssi, timestamp = details
        display.show(msg, rssi, timestamp)
