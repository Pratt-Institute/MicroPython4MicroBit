import radio
from microbit import *

# The radio won't work unless it's switched on.
radio.on()

# keep score
messages_rec = 0

# Event loop.
while True:
    # Button A sends ping
    if button_a.was_pressed():
        radio.send('ping')
    # Button A sends ping
    if button_b.was_pressed():
        display.scroll(messages_rec)
    # Read any incoming messages.
    incoming = radio.receive()
    if incoming == 'ping':
        pin0.write_digital(1)  # turn pin0 (and the LED) on
        sleep(500)             # delay for half a second (500 milliseconds)
        pin0.write_digital(0)  # turn pin0 (and the LED) off
        messages_rec += 1