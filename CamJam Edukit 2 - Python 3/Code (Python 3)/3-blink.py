# CamJam Edukit 1 - Basics
# Worksheet 3 - Blinking LED

# Import Libraries
import time             # A collection of time related commands
import RPi.GPIO as GPIO # The GPIO commands

# Set the GPIO pin naming mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set pins 18, 23 and 24 to be output
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

# Turn LEDs on
GPIO.output(18, GPIO.HIGH)
GPIO.output(23, GPIO.HIGH)
GPIO.output(24, GPIO.HIGH)

time.sleep(1) # Pause for 1 second

# Turn LEDs off
GPIO.output(18, GPIO.LOW)
GPIO.output(23, GPIO.LOW)
GPIO.output(24, GPIO.LOW)

time.sleep(1) # Pause for 1 second

# Turn LEDs on
GPIO.output(18, GPIO.HIGH)
GPIO.output(23, GPIO.HIGH)
GPIO.output(24, GPIO.HIGH)

time.sleep(1) # Pause for 1 second

# Turn LEDs off
GPIO.output(18, GPIO.LOW)
GPIO.output(23, GPIO.LOW)
GPIO.output(24, GPIO.LOW)

# Clean up the GPIO pins
GPIO.cleanup()