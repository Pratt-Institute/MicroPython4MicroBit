from servo_lib import *

# Start at 0 degrees
Servo(pin0).write_angle(0)
sleep(1000)

while True:
    Servo(pin0).write_angle(0)
    sleep(1000)
    Servo(pin0).write_angle(90)
    sleep(1000)
    Servo(pin0).write_angle(180)
    sleep(1000)
