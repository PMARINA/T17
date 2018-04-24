import sensor
import motor
import versaValve
import camera
import time


class Robot:
    global leftSensor
    global rightSensor
    global frontSensor

    global leftMotor
    global rightMotor

    global vv
    global camera

    def __init__(self):
        self.frontSensor = sensor.Sensor(23, 24)
        self.leftSensor = sensor.Sensor(17, 27)
        self.rightSensor = sensor.Sensor(5, 6)

        self.leftMotor = motor.Motor(0)
        self.rightMotor = motor.Motor(1)

        self.vv = versaValve.Versa()
        self.cam = camera.Camera()
        print("Robot intialized")

    def forwards(self):
        self.leftMotor.run(7000)
        self.rightMotor.run(1000)

    def turnRight(self):
        self.leftMotor.run(7000)
        self.rightMotor.run(0)

    def turnLeft(self):
        self.leftMotor.run(1000)
        self.rightMotor.run(7000)

    def backwards(self):
        self.leftMotor.run(7000)
        self.rightMotor.run(1000)

    def pressureCheck(self):
        self.vv.open()
        time.sleep(0.5)
        self.vv.close()

    def extinguish(self):
        self.vv.open()
        time.sleep(10)
        self.vv.close()

    def stop(self):
        self.leftMotor.run(0)
        self.rightMotor.run(0)

    def testMotors(self):
        self.forwards()
        time.sleep(1)
        self.stop()
        time.sleep(1)
        self.backwards()
        time.sleep(1)
        self.stop()
    def printSensors():
        print("Left: " + self.leftSensor.
