# CamJam EduKit 1 – Basic
# Worksheet 2 – LEDs

# Import Libraries 
import time  # A collection of time related commands 
from picozero import LED  # The LED function from picozero

# Set pins 15, 14 and 13 to be LEDs
red = LED(15)
yellow = LED(14)
green = LED(13)

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
