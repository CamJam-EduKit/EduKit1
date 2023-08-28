# CamJam EduKit 1 – Basic
# Worksheet 4 – User Input

# Import Libraries
import time  # A collection of time related commands
from picozero import LED  # The LED function from picozero 

# Set pins 15, 14 and 13 to be LEDs
red = LED(15)
yellow = LED(14)
green = LED(13)

# Ask the user the colour LED to blink.
print("Which LED would you like to blink?")
print("1: Red?")
print("2: Yellow?")
print("3: Green?")

# Click on the space after : in the Shell area
# to move the cursor to correct position.
led_choice = input("Choose your option: ")

# Ensure that the led_choice variable is a whole number (integer)
led_choice = int(led_choice)

# Ask the user how many times they want the LED to blink.
count = input("How many times would you like it to blink? ")

# Ensure that the count variable is a whole number (integer)
count = int(count)

# Sets the variable 'LEDChoice' to be the LED choice
if led_choice == 1:
    print("You picked the Red LED")
    led_chosen = red
elif led_choice == 2:
    print("You picked the Yellow LED")
    led_chosen = yellow
elif led_choice == 3:
    print("You picked the Green LED")
    led_chosen = green
else:
    print("")

# If we have chosen a valid choice, flash the LED
if led_choice > 0:
    # While the count variable is greater than zero
    while count > 0:
        led_chosen.on()  # Turn the chosen LED on
        time.sleep(1)  # Sleep for 1 second
        led_chosen.off()  # Turn the chosen LED off
        time.sleep(2)  # Sleep for 2 seconds
        count = count - 1  # Decrease the count by one
