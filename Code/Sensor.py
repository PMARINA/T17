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
        #depends on what sensor we use
        #implement later
        #Also, do calibration depending on pi's accuracy (timewise)
    def getDistance(self):
        dist=self.calcDistance()
        return dist
