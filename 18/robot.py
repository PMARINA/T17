import sensor
import motor
import versaValve
import camera
import time


class Robot:
    leftSensor = sensor.Sensor(23, 24)
    rightSensor = sensor.Sensor(17, 27)
    frontSensor = sensor.Sensor(5, 6)

    leftMotor = motor.Motor(0)
    rightMotor = motor.Motor(1)

    versaValve = Versa()
    camera = camera.Camera()
        def __init__(self):
            print("Robot intialized")

    def forwards():
        leftMotor.run(7000)
        rightMotor.run(1000)

    def turnRight():
        leftMotor.run(7000)
        rightMotor.run(0)
        time.sleep(1)

    def turnLeft():
        leftMotor.run(1000)
        rightMotor.run(7000)

    def extinguish():
        versaValve.open()
        time.sleep(10)
        versaValve.close()

    def stop():
        leftMotor.run(0)
        rightMotor.run(0)
