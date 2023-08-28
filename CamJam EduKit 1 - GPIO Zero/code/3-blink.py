# CamJam EduKit 1 – Basics
# Worksheet 3 – Blinking LED

# Import Libraries
import time  # A collection of time related commands
from gpiozero import LED  # The LED functions from GPIO Zero

# Set pins 18, 23 and 24 to be LEDs
red = LED(18)
yellow = LED(23)
green = LED(24)

# Turn LEDs on
red.on()
yellow.on()
green.on()

time.sleep(1)  # Pause for 1 second

# Turn LEDs off
red.off()
yellow.off()
green.off()

time.sleep(1)  # Pause for 1 second

# Turn LEDs on
red.on()
yellow.on()
green.on()

time.sleep(1)  # Pause for 1 second

# Turn LEDs off
red.off()
yellow.off()
green.off()
