# CamJam EduKit 1 - Basics
# Worksheet 5 - Button

# Import Libraries
import os  # Gives Python access to Linux commands
import time  # Proves time related commands
import RPi.GPIO as GPIO  # Gives Python access to the GPIO pins

GPIO.setmode(GPIO.BCM)  # Set the GPIO pin naming mode
GPIO.setwarnings(False)  # Suppress warnings

# Set pin 25 as an input pin
ButtonPin = 25
GPIO.setup(ButtonPin, GPIO.IN)

print("---------------")
print(" Button + GPIO ")
print("---------------")

print(GPIO.input(ButtonPin))

# The commands indented after this 'while' will be repeated
# forever or until 'Ctrl+c' is pressed.
while True:
    # If the button is pressed, ButtonPin will be 'false'
    if GPIO.input(ButtonPin) == False:
        print("Button Pressed")
        print(GPIO.input(ButtonPin))
        time.sleep(1)  # Sleep for 1 second
    else:
        os.system('clear')  # Clears the Terminal Window
        print("Waiting for you to press the button")

    time.sleep(0.5)  # Sleep for 0.5 seconds
