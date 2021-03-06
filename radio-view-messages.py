# Simple radio example
# Adapted from https://microbit-micropython.readthedocs.io/en/latest/radio.html
import radio
from microbit import *

# The radio won't work unless it's switched on.
radio.on()
radio.config(channel=7)

# Event loop.
while True:
    incoming = radio.receive()
    if incoming:
        display.show(incoming)