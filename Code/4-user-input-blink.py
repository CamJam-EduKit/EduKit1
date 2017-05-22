# CamJam Edukit 1 - Basics
# Worksheet 4 - User Input

# Load Libraries
import os                # Allows you to interact with the operating system
import time              # A collection of time related commands
from gpiozero import LED # The LED functions from GPIO Zero

GPIO.setmode(GPIO.BCM) # Set the GPIO pin naming mode
GPIO.setwarnings(False) # Supress warnings

# Set up variables to store the pin numbers
LEDRed = 18
LEDYellow = 23
LEDGreen = 24

# Set the LED pins to output
GPIO.setup(LEDRed, GPIO.OUT)
GPIO.setup(LEDYellow, GPIO.OUT)
GPIO.setup(LEDGreen, GPIO.OUT)

os.system('clear') # Clears the terminal window

# Ask the user which colour LED to blink 
print("Which LED would you like to blink")
print("1: Red?")
print("2: Yellow?")
print("3: Green?")
led_choice = input("Choose your option: ")
# Ensure that the led_choice variable is a whole number (integer)
led_choice = int(led_choice)

# Ask the user how many times they want the LED to blink
count = input("How many times would you like it to blink?: ")
# Ensure that the count variable is a whole number (integer)
count = int(count)

# Set the LEDChoice variable depending on the LED choice
if led_choice == 1:
    print("You picked the Red LED")
    LEDChoice = LEDRed
if led_choice == 2:
    print("You picked the Yellow LED")
    LEDChoice = LEDYellow
if led_choice == 3:
    print("You picked the Green LED")
    LEDChoice = LEDGreen

# If we have chosen a valid choice, flash the LED
if LEDChoice > 0:
    while count > 0:
        GPIO.output(LEDChoice, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LEDChoice, GPIO.LOW)
        time.sleep(1)
        count = count - 1

GPIO.cleanup()