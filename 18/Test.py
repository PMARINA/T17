import RPi.GPIO as GPIO
import Sensor

s1 = Sensor.Sensor(19, 26)
print(s1.distance())
print(GPIO.cleanup())
