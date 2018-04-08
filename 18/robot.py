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

        forwards():
            leftMotor.run(7000)
            rightMotor.run(1000)
        turnRight():
            leftMotor.run(7000)
            rightMotor.run(0)
            time.sleep(1)
