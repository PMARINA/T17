# Libraries
import time

import RPi.GPIO as GPIO


class Sensor:
    GPIO_TRIGGER = -1
    GPIO_ECHO = -1

    def __init__(self, echo, trigger):
        GPIO.setmode(GPIO.BCM)

        # set GPIO Pins
        self.GPIO_TRIGGER = trigger  # 9#23 #24
        self.GPIO_ECHO = echo  # 0#16 #12

        # set GPIO direction (IN / OUT)
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)

    def distance(self):
        # set Trigger to HIGH
        GPIO.output(self.GPIO_TRIGGER, True)

        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.GPIO_TRIGGER, False)

        StartTime = time.time()
        StopTime = time.time()

        # save StartTime
        while GPIO.input(self.GPIO_ECHO) == 0:
            StartTime = time.time()

        # save time of arrival
        while GPIO.input(self.GPIO_ECHO) == 1:
            StopTime = time.time()

        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2

        return distance


# Main code only to be run for diagnostics
if __name__ == '__main__':
    try:
        s1 = Sensor(19, 26)  # Hardcoded pin numbers, change if applicable
        while True:
            dist = s1.distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
