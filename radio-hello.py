# Simple radio example
# Adapted from https://microbit-micropython.readthedocs.io/en/latest/radio.html
import radio
from microbit import *

# The radio won't work unless it's switched on.
radio.on()

# Event loop.
while True:
    # Button A sends a "hello" message.
    if button_a.was_pressed():
        radio.send('hello')
    # Read any incoming messages.
    incoming = radio.receive()
    if incoming == 'hello':
        # Show happy face if received hello 
        display.show(Image.HAPPY, delay=100, wait=False)
