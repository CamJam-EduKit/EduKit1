# CamJam Edukit 1 - Basics
# Worksheet 7 - Traffic Lights - Solution

# Import Libraries
import os
import time
from gpiozero import LED, Button, Buzzer

# Set up variables for the LED, Buzzer and switch pins
green = LED(24)
yellow = LED(23)
red = LED(18)
buzzer = Buzzer(22)
button = Button(25)

# Define a function for the initial state (Green LED on, rest off)
# (If you have the second 'pedestrian LEDs, turn the red on & green
# off)
def StartGreen():
    print("Green light on")
    green.on()
    yellow.off()
    red.off()

# Turn the green off and the amber on for 3 seconds
# ('Pedestrian' red LED stays lit)
def SteadyAmber():
    print("Steady amber")
    green.off()
    yellow.on()
    red.off()
    time.sleep(3)

# Turn the amber off, and then the red on for 1 second
def SteadyRed():
    print("Steady red")
    green.off()
    yellow.off()
    red.on()
    time.sleep(1)

# Sound the buzzer for 4 seconds
# (If you have the 'pedestrian' LEDs, turn the red off and green on)
def StartWalking():
    # Make the buzzer buzz on and off, half a second of
    # sound followed by half a second of silence
    print("Start walking")
    iCount = 1
    while iCount <= 4:
        print("Beep")
        buzzer.on()
        time.sleep(0.5)
        buzzer.off()
        time.sleep(0.5)
        iCount += 1

# Turn the buzzer off and wait for 2 seconds
# (If you have a second green 'pedestrian' LED, make it flash on and
# off for the two seconds)
def DontWalk():
    print("Dont walk")
    buzzer.off()

# Flash the amber on and off for 6 seconds
# (And the green 'pedestrian' LED too)
def FlashingAmberGreen():
    print("Flashing amber and green")
    red.off()
    green.off()

    iCount = 1
    while iCount <= 6:
        yellow.on()
        time.sleep(0.5)
        yellow.off()
        time.sleep(0.5)
        iCount += 1
    green.on()

# Flash the amber for one more second
# (Turn the green 'pedestrian' LED off and the red on)
def FlashingAmber():
    print("Flashing amber")

    green.off()

    yellow.on()
    time.sleep(0.5)
    yellow.off()
    time.sleep(0.5)

    red.on()

# Go through the traffic light sequence by calling each function
# one after the other.
def TrafficLightSequence():
    print("Traffic Light sequence started")
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

waiting_time = 20

# Here is the loop that waits at lease 20 seconds before
# stopping the cars if the button has been pressed
while True: # Loop around forever
    ButtonNotPressed = True # Button has not been pressed
    start = time.time() # Records the current time 
    while ButtonNotPressed: # While the button has not been pressed
        time.sleep(0.1) # Wait for 0.1s
        if (button.ispressed): # If the button is pressed
            print("Button has been pressed")
            now = time.time()
            ButtonNotPressed = False # Button has been pressed
            if (now-start) <= waiting_time: # If under 20 seconds
                time.sleep(waiting_time - (now-start)) # Wait until 20s is up
            TrafficLightSequence() # Run the traffic light sequence
