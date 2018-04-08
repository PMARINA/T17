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

    vv = versaValve.Versa()
    camera = camera.Camera()

    def __init__(self):
        leftSensor = sensor.Sensor(23, 24)
        rightSensor = sensor.Sensor(17, 27)
        frontSensor = sensor.Sensor(5, 6)

        leftMotor = motor.Motor(0)
        rightMotor = motor.Motor(1)

        vv = versaValve.Versa()
        camera = camera.Camera()
        print("Robot intialized")

    def forwards(self):
        leftMotor.run(7000)
        rightMotor.run(1000)

    def turnRight(self):
        leftMotor.run(7000)
        rightMotor.run(0)
        time.sleep(1)

    def turnLeft(self):
        leftMotor.run(1000)
        rightMotor.run(7000)

    def backwards(self):
        leftMotor.run(7000)
        rightMotor.run(1000)

    def pressureCheck(self):
        vv.open()
        time.sleep(0.5)
        vv.close()

    def extinguish(self):
        vv.open()
        time.sleep(10)
        vv.close()

    def stop(self):
        leftMotor.run(0)
        rightMotor.run(0)

    def testMotors(self):
        forwards()
        time.sleep(1)
        stop()
        time.sleep(1)
        backwards()
        time.sleep(1)
        stop()
