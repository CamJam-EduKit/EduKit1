# CamJam Edukit 1 - Basics
# Worksheet 3 - Blink LED Forever

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

# Loop forever (as true is always true)
while True:
    # Turn LEDs on
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.HIGH)

    # Wait one second
    time.sleep(1)

    # Turn LEDs off
    GPIO.output(18, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)

    # Wait one second
    time.sleep(1)