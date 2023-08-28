# CamJam EduKit 1 – Basic
# Worksheet 2 – Onboard LEDs for Raspberry Pi Pico.

# Import Libraries
import time  # A collection of time related commands
from picozero import pico_led  # The onboard LED function from picozero

print("LEDs on")
pico_led.on()

print("Wait for one second")
time.sleep(1)

print("LEDs off")
pico_led.off()
