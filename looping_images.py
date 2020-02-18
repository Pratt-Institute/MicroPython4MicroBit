from microbit import *

myimgs = [Image.NO, Image.YES]

# Loop images using display.show
display.show(myimgs, loop=False, delay=400)

while True:
    # loop images using for loop and array
    for item in range(0, len(myimgs)):
        display.show(myimgs[item])
        sleep(400)
