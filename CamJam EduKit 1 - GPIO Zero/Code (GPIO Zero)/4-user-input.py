# CamJam EduKit 1 – Basics
# Worksheet 4 – User Input

# Import Libraries
import os  # Allows interaction with the operating system
import time  # A collection of time related commands
from gpiozero import LED  # The LED functions from GPIO Zero

# Set pins 18, 23 and 24 to be LEDs
red = LED(18)
yellow = LED(23)
green = LED(24)

os.system('clear')  # Clears the terminal window

# Ask the user, which colour LED to blink
print("Which LED would you like to blink?")
print("1: Red?")
print("2: Yellow?")
print("3: Green?")
led_choice = input("Select your option: ")
# Ensure that the led_choice variable is a whole number (integer)
led_choice = int(led_choice)

# Ask the user how many times they want the LED to blink.
count = input("How many times would you like it to blink?")
# Ensure that the count variable is a whole number (integer)
count = int(count)

# Sets the variable 'LEDChoice' to be the LED choice
if led_choice == 1:
    print("You picked the Red LED")
    LEDChoice = red
elif led_choice == 2:
    print("You picked the Yellow LED")
    LEDChoice = yellow
elif led_choice == 3:
    print("You picked the Green LED")
    LEDChoice = green

# If we have chosen a valid choice, flash the LED
if led_choice > 0:
    # While the count variable is greater than zero
    while count > 0:
        LEDChoice.on()  # Turn the chosen LED on
        time.sleep(1)  # Sleep for 1 second
        LEDChoice.off()  # Turn the chosen LED off
        time.sleep(2)  # Sleep for 2 seconds
        count -= 1  # Decrease the count by one
