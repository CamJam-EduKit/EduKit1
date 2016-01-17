# Import Libraries
import os
import time
import RPi.GPIO as GPIO

# Set the GPIO pin naming mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PINBuzzer = 22 # Sets the buzzer pin 22

# Sets PINBuzzer as an output pin and initialise it to 'off'
GPIO.setup(PINBuzzer, GPIO.OUT)
GPIO.output(PINBuzzer, GPIO.LOW)

def dot(): # A single Morse dot
    GPIO.output(PINBuzzer, GPIO.HIGH)
    time.sleep(.1)
    GPIO.output(PINBuzzer, GPIO.LOW)
    time.sleep(.1)

def dash(): # A single Morse dash
    GPIO.output(PINBuzzer, GPIO.HIGH)
    time.sleep(.3)
    GPIO.output(PINBuzzer, GPIO.LOW)
    time.sleep(.1)

def letterSpace(): # The space between letters
    time.sleep(.2)

def wordSpace(): # The space between words
    time.sleep(.6)

def morseS(): # The Morse for S, ...
    dot()
    dot()
    dot()

def morseO(): # The Morse for O, ---
    dash()
    dash()
    dash()

os.system('clear') # Clears the screen
print("Morse Code")
# Prompt
loop_count = input("How many times would you like SOS to loop?: ")
loop_count = int(loop_count)

while loop_count > 0: # Loop around the chosen number of times
    loop_count = loop_count - 1
    morseS()
    letterSpace()
    morseO()
    letterSpace()
    morseS()
    wordSpace()

GPIO.cleanup()
