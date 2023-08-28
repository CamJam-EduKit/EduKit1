# CamJam EduKit 1 – Basic
# Worksheet 5 – Button

# Import Libraries
import time  # Proves time related commands
from picozero import Button  # The picozero button function

# Set pin 12 as a button input
button = Button(12)

print("-------------")
print("Button + GPIO")
print("-------------")

# The commands indented after this ‘while’ will be repeated
# forever or until ‘Ctrl+c’ is pressed.
while True:
    # If the button is pressed, button.is_pressed will be 'true'
    if button.is_pressed:
        print("Button pressed")
        time.sleep(1)  # Sleep for 1 second
    else:
        print("Waiting for you to press the button")

    time.sleep(0.5)  # Sleep for 0.5 seconds
