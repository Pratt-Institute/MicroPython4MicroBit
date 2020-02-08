from microbit import *

while True:
    value = pin0.read_analog()
    print((value,))
    sleep(100)
    # Open the plotter button to see values change


