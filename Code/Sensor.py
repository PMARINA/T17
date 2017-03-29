import RPi.GPIO as GPIO
import time
class Sensor:
    def __init__(self,trig,ech):
        self.trigger=trig
        self.echo=ech
    def getTime(self):
        GPIO.setmode(GPIO.BOARD)#move to constructor?
        GPIO.setup(self.trigger,GPIO.OUT)
        GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.output(self.trigger,TRUE)
        millis1=int(round(time.time()*1000))
        while TRUE:
            if GPIO.input(self.echo):
                break;
        millis2=int(round(time.time()*1000))
        return millis2-millis1
    def calcDistance(self):
        dist1=self.getTime()*0.028+1.093
        return dist1
    def getDistance(self):
        dist=self.calcDistance()
        return dist
