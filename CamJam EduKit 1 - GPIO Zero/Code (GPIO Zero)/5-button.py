# CamJam Edukit 1 - Basics
# Worksheet 5 - Button

# Import Libraries
import os                   # Gives Python access to Linux commands
import time                 # Proves time related commands
from gpiozero import Button # The GPIO Zero button functions

# Set pin 25 as a button input
button = Button(25)

print("---------------")
print(" Button + GPIO ")
print("---------------")

# The commands indented after this ‘while’ will be repeated
# forever or until ‘Ctrl+c’ is pressed.
while True:
    # If the button is pressed, button.is_pressed will be 'true'
    if (button.is_pressed):
        print("Button Pressed")
        time.sleep(1) # Sleep for 1 second
    else:
        os.system('clear') # Clears the Terminal Window
        print("Waiting for you to press the button")
        
    time.sleep(0.5) # Sleep for 0.5 seconds