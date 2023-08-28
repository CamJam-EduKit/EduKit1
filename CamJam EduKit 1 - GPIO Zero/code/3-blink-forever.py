# CamJam EduKit 1 – Basics
# Worksheet 3 – Blink LED Forever

# Import Libraries
import time  # A collection of time related commands
from gpiozero import LED  # The LED functions from the GPIO Zero library

# Set pins 18, 23 and 24 to be LEDs
red = LED(18)
yellow = LED(23)
green = LED(24)

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
