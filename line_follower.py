import pi2go
import time
import RPi.GPIO as GPIO

# Initialize Pi2Go and GPIO
pi2go.init()
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for LDR sensors
left_ldr_pin = 17
right_ldr_pin = 18

# Set LDR pins as input
GPIO.setup(left_ldr_pin, GPIO.IN)
GPIO.setup(right_ldr_pin, GPIO.IN)

# Here we set the speed to 60 out of 100 - feel free to change!
speed = 60

try:
    while True:
        # Read LDR sensor values
        left = GPIO.input(left_ldr_pin)
        right = GPIO.input(right_ldr_pin)

        if left == right:  # If both sensors are the same (either on or off):
            # Forward
            pi2go.forward(speed)
        elif left == 1:  # If the left sensor is on
            # Left
            pi2go.spinRight(speed)
        elif right == 1:  # If the right sensor is on
            # Right
            pi2go.spinLeft(speed)

finally:  # Even if there was an error, cleanup
    pi2go.cleanup()
    GPIO.cleanup()
