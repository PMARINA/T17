import RPi.GPIO as GPIO


class Versa:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(21, GPIO.OUT)

    def open(self):
        GPIO.output(21, GPIO.LOW)

    def close(self):
        GPIO.output(21, GPIO.HIGH)
