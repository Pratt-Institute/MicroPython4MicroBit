import radio
from microbit import *

# The radio won't work unless it's switched on.
radio.on()
radio.config(channel=7)

# keep score
messages_rec = 0

# Event loop.
while True:
    # Button A sends ping
    if button_a.was_pressed():
        radio.send('ping')
    # Button B prints total so far 
    if button_b.was_pressed():
        display.scroll(messages_rec)
    # Read any incoming messages.
    incoming = radio.receive()
    if incoming == 'ping':
        display.show(Image.SQUARE_SMALL, delay=100, wait=False, clear=True)
        messages_rec += 1