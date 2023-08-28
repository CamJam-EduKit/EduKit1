# CamJam EduKit 1 – Basic
# Worksheet 3 – Blink LED Forever

# Import Libraries
import time  # A collection of time related commands
from picozero import LED  # The LED function from picozero

# Set pins 15, 14 and 13 to be LEDs
red = LED(15)
yellow = LED(14)
green = LED(13)

# Loop forever (as true is always true)
while True:
    # Turn LEDs on
    red.on()
    yellow.on()
    green.on()

    # Wait for one second
    time.sleep(1)

    # Turn LEDs off
    red.off()
    yellow.off()
    green.off()

    # Wait for one second
    time.sleep(1)
