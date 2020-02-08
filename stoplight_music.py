from microbit import *
import music

# Turn all LED off to start
pin1.write_digital(0)
pin2.write_digital(0)
pin8.write_digital(0)

while True:
    # Green on, safe to cross
    pin1.write_digital(1)
    music.play(music.ENTERTAINER)
    sleep(5000)
    # Turn off
    pin1.write_digital(0)
    # Yellow on, play warning
    pin2.write_digital(1)
    music.play(music.CHASE)
    sleep(3000)
    # Turn off
    pin2.write_digital(0)
    # Green light on
    pin8.write_digital(1)
    sleep(10000)
    # Turn off
    pin8.write_digital(0)

