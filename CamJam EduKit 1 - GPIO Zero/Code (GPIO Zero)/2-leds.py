# CamJam Edukit 1 - Basics
# Worksheet 2 - LEDs

# Import Libraries
import time              # A collection of time related commands
from gpiozero import LED # The LED functions from GPIO Zero

# Set pins 18, 23 and 24 to be LEDs
red = LED(18)
yellow = LED(23)
green = LED(24)

print("LEDs on")
red.on()
yellow.on()
green.on()

print("Wait for one second")
time.sleep(1)

print("LEDs off")
red.off()
yellow.off()
green.off()