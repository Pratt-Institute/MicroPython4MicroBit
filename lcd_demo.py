# Adapted from:
# https://github.com/shaoziyang/microbit-lib/tree/master/lcd/I2C_LCD1602

from mb_i2c_lcd1602 import *

lcd=LCD1620()

while True:
    # Print to both lines of LCD
    lcd.puts('Hello', 0, 0)
    lcd.puts('World!', 1, 5)
    sleep(1000)
    # Clear screen
    lcd.clear()
    sleep(1000)
    # Turn backlight off and on again
    lcd.backlight(1)
    sleep(1000)
    lcd.backlight(0)
    sleep(1000)
    lcd.backlight(1)
    sleep(1000)

