# CamJam Edukit 1 – Basic
# Worksheet 6 – Morse Code

# Import Libraries
import time  # Proves time related commands
from picozero import Buzzer  # The picozero buzzer functions

# Set pin 11 as a buzzer
buzzer = Buzzer(11)


# Define some 'user-defined functions'
def dot():  # A single Morse dot
    buzzer.on()
    time.sleep(0.1)
    buzzer.off()
    time.sleep(0.1)


def dash():  # A single Morse dash
    buzzer.on()
    time.sleep(0.3)
    buzzer.off()
    time.sleep(0.1)


def letterSpace():  # The space between letters
    time.sleep(0.2)


def wordSpace():  # The space between words
    time.sleep(0.6)


def morseS():  # The Morse for S, ...
    dot()
    dot()
    dot()


def morseO():  # The Morse for O, ---
    dash()
    dash()
    dash()


print("Morse Code")

# Prompt the user for input
loop_count = input("How many times would you like SOS to loop? ")
loop_count = int(loop_count)  # Convert text to an integer

while loop_count > 0:  # Loop around the chosen amount
    morseS()
    letterSpace()
    morseO()
    letterSpace()
    morseS()
    wordSpace()
    loop_count -= 1
