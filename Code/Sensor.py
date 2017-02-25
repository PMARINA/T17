import RPi.GPIO as GPIO
import time
class Sensor:
    trigger=0
    echo=0
    def _init_(trig,ech):
        trigger=trig
        echo=ech
    def getTime():
        GPIO.setmode(GPIO.BOARD)#move to constructor?
        GPIO.setup(trigger,GPIO.OUT)
        GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.output(trigger,TRUE)
        millis1=int(round(time.time()*1000))
        while TRUE:
            if GPIO.input(echo):
                break;
        millis2=int(round(time.time()*1000))
        return millis2-millis1
    def calcDistance():
        #depends on what sensor we use
        #implement later
        
