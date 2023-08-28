# CamJam EduKit 1 – Basic
# Worksheet 3 – Blinking LED

# Import Libraries
import time  # A collection of time related commands
from picozero import LED  # The LED function from picozero

# Set pins 15, 14 and 13 to be LEDs
red = LED(15)
yellow = LED(14)
green = LED(13)

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
