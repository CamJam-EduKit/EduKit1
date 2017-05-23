# CamJam Edukit 1 - Basics
# Worksheet 7 - Traffic Lights - Solution

# Import Libraries
import os
import time
import RPi.GPIO as GPIO

# Set the GPIO pin naming mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set up variables for the LED, Buzzer and switch pins
PinGreen = 24
PinAmber = 23
PinRed = 18
PinBuzzer = 22
PinButton = 25
# PinGreenPedestrian = 17
# PinRedPedestrian = 27

# Set up each of the input (switch) and output (LEDs, Buzzer) pins
GPIO.setup(PinGreen, GPIO.OUT)
GPIO.setup(PinAmber, GPIO.OUT)
GPIO.setup(PinRed, GPIO.OUT)
GPIO.setup(PinBuzzer, GPIO.OUT)
GPIO.setup(PinButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(PinGreenPedestrian, GPIO.OUT)
#GPIO.setup(PinRedPedestrian, GPIO.OUT)

GPIO.output(PinGreen, GPIO.LOW)
GPIO.output(PinAmber, GPIO.LOW)
GPIO.output(PinRed, GPIO.LOW)
GPIO.output(PinBuzzer, GPIO.LOW)
#GPIO.output(PinGreenPedestrian, GPIO.LOW)
#GPIO.output(PinRedPedestrian, GPIO.LOW)

# Define a function for the initial state (Green LED on, rest off)
# (If you have the second 'pedestrian LEDs, turn the red on & green
# off)
def StartGreen():
    # Remember all code in the function is indented
    GPIO.output(PinGreen, GPIO.HIGH)
    # GPIO.output(PinRedPedestrian, GPIO.HIGH)

# Turn the green off and the amber on for 3 seconds
# ('Pedestrian' red LED stays lit)
def SteadyAmber():
    # Remember all code in the function is indented
    GPIO.output(PinGreen, GPIO.LOW)
    GPIO.output(PinAmber, GPIO.HIGH)
    time.sleep(3)

# Turn the amber off, and then the red on for 1 second
def SteadyRed():
    # Remember all code in the function is indented
    GPIO.output(PinAmber, GPIO.LOW)
    GPIO.output(PinRed, GPIO.HIGH)
    time.sleep(1)

# Sound the buzzer for 4 seconds
# (If you have the 'pedestrian' LEDs, turn the red off and green on)
def StartWalking():
    # Make the buzzer buzz on and off, half a second of
    # sound followed by half a second of silence
    # GPIO.output(PinRedPedestrian, GPIO.LOW)
    # GPIO.output(PinGreenPedestrian, GPIO.HIGH)
    iCount = 1
    while iCount <= 4:
        GPIO.output(PinBuzzer, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(PinBuzzer, GPIO.LOW)
        time.sleep(0.5)
        iCount += 1

# Turn the buzzer off and wait for 2 seconds
# (If you have a second green 'pedestrian' LED, make it flash on and
# off for the two seconds)
def DontWalk():
    # Remember all code in the function is indented
    GPIO.output(PinBuzzer, GPIO.LOW)
    iCount = 1
    while iCount <= 2:
        #GPIO.output(PinGreenPedestrian, GPIO.HIGH)
        time.sleep(0.5)
        #GPIO.output(PinGreenPedestrian, GPIO.LOW)
        time.sleep(0.5)
        iCount += 1

# Flash the amber on and off for 6 seconds
# (And the green 'pedestrian' LED too)
def FlashingAmberGreen():
    # Remember all code in the function is indented
    GPIO.output(PinRed, GPIO.LOW)
	
    iCount = 1
    while iCount <= 6:
        GPIO.output(PinAmber, GPIO.HIGH)
        # GPIO.output(PinGreenPedestrian, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(PinAmber, GPIO.LOW)
        # GPIO.output(PinGreenPedestrian, GPIO.LOW)
        time.sleep(0.5)
        iCount += 1

# Flash the amber for one more second
# (Turn the green 'pedestrian' LED off and the red on)
def FlashingAmber():
    # Remember all code in the function is indented
    # GPIO.output(PinRedPedestrian, GPIO.HIGH)
    GPIO.output(PinAmber, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(PinAmber, GPIO.LOW)
    time.sleep(0.5)

# Go through the traffic light sequence by calling each function
# one after the other.
def TrafficLightSequence():
    # Remember all code in the function is indented
    # Green will already be on
    SteadyAmber()
    SteadyRed()
    StartWalking()
    DontWalk()
    FlashingAmberGreen()
    FlashingAmber()
    StartGreen()

os.system('clear') # Clears the terminal
print("Traffic Lights")
# Initialise the traffic lights
StartGreen()

# Here is the loop that waits at lease 20 seconds before
# stopping the cars if the button has been pressedS
while True: # Loop around forever
    ButtonNotPressed = True # Button has not been pressed
    start = time.time() # Records the current time (seconds since 1st January 1970)
    while ButtonNotPressed: # While the button as not been pressed
        time.sleep(0.1) # Wait for 0.1s
        if GPIO.input(PinButton) == False: # If the button is pressed
            print("Button has been pressed")
            now = time.time()
            ButtonNotPressed = False # Button has been pressed
            if (now - start) <= 20: # If under 20 seconds
                time.sleep (20 - (now - start)) # Wait until 20s is up
            TrafficLightSequence() # Run the traffic light sequence

GPIO.cleanup()