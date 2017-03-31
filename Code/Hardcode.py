dogPos =-1
front = Sensor.__init__(0,0)
left = Sensor.__init__(0,0)
right = Sensor.__init__(0,0)
leftM = Motor.__init__(input)
rightM = Motor.__init__(input)
if front.calcDistance()<50:
    #Dog in front, facing right
    process1()
    if checkDone():
        sys.exit()
    process2()

elif left.calcDistance()<10:
    #Facing right, no dog in front
    dogPos2()
else:
    turnLeft()
    dogPos2()

def dogPos2():
    while(front.calcDistance()>69):
        forwards();
    stop()
    turnRight()
    while front.calcDistance()>51:
        forwards()
    stop()
    scanRoom()
    if checkDone():
        return
    while front.calcDistance<74:
        backwards()
    stop()
    while front.calcDistance()>26:
        forwards()
    stop()
    turnRight()
    if front.calcDistance()<200:
        #Dog in pos2
        process2()
    if checkDone():
        return
def process2():
    turnRight()
    while front.calcDistance()>23:
        forwards()
    stop()
    turnLeft()
    while front.calcDistance()>118:
        forwards()
    stop()
    turnLeft()
    while front.calcDistance()>23:
        forwards()
    stop()
    turnRight()
    while front.calcDistance()>47:
        forwards()
    stop()
    scanRoom()
    if checkDone():
        return
    while front.calcDistance()>15:
        forwards()
    stop()
    turnLeft()
    while front.calcDistance()>23:
        forwards()
    stop()
    turnRight()
    while front.calcDistance()>65:
        forwards()
    stop()
    scanRoom()
    if checkDone():
        return
    while front.calcDistance()<98:
        backwards()
    stop()
    turnRight()
    while front.calcDistance()>118:
        forwards()
    stop()
    turnLeft()
    while front.calcDistance()>23:
        forwards()
    stop()
    turnright()
    sys.exit() #Done with maze, fire not found, if the thing has not finished by now
def process1():
    while front.calcDistance()>126:
        forwards()
    stop()
    turnLeft()
    while front.calcDistance()>23:
        forwards()
    stop()
    turnLeft()
    while front.calcDistance()>23:
        forwards()
    stop()
    turnLeft()
    triggerDistance = left.calcDistance()
    while left.calcDistance()>=triggerDistance-10:
        forwards()
    stop()
    turnLeft()
    while front.calcDistance>47:
        forwards()
    stop()
    scanRoom()
    if checkDone():
        return
    while front.calcDistance<74:
        backwards()
    stop()
    turnLeft()
    while front.calcDistance>23:
        forwards()
    stop()
    turnRight()
    process3()
def process3():
	#copy parts of process2 into here, from where it circumnavigates the dog triangle...
def forwards():
    leftM.forward()
    rightM.forward()
def backwards():
    leftM.back()
    rightM.back()
def stop():
    leftM.stop()
    rightM.stop()
