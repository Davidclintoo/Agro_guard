from gpiozero import Robot
import time
import RPi.GPIO as GPIO

# Initialize GPIO
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for LDR sensors
left_ldr_pin = 17
right_ldr_pin = 18

# Set LDR pins as input
GPIO.setup(left_ldr_pin, GPIO.IN)
GPIO.setup(right_ldr_pin, GPIO.IN)

# Initialize the robot
robot = Robot(left=(23, 24), right=(17, 18))

# Here we set the speed to 60 out of 100 - feel free to change!
speed = 0.6

try:
    while True:
        # Read LDR sensor values
        left = GPIO.input(left_ldr_pin)
        right = GPIO.input(right_ldr_pin)

        if left == right:  # If both sensors are the same (either on or off):
            # Forward
            robot.forward(speed)
        elif left == 1:  # If the left sensor is on
            # Left
            robot.right(speed)
        elif right == 1:  # If the right sensor is on
            # Right
            robot.left(speed)

finally:  # Even if there was an error, cleanup
    robot.stop()
    GPIO.cleanup()
