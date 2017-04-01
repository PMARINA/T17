dogPos=-1
front = Sensor.__init__(0,0)
left = Sensor.__init__(0,0)
right = Sensor.__init__(0,0)
leftM = Motor.__init__(input)
rightM = Motor.__init__(input)
#........1...
#...........2  <-- Dog positiions
#.........3..

#2......1
#3......4 <-- Room numbers
flame=True
               

def position1():#starts at very beginning
    while front.calcDistance()>129:#facing south in center hallway
        forwards()
    turnRight()
    while front.calcDistance()>25:#facing west going towards entrance of room 2
        forwards()
    turnRight()
    while front.calcDistance()>80:#move forward a bit into room2
        forwards()
    stop()
    scanRoom2()#scan room 2
    if flame==False:
        killmovement()
    while front.calcDistance()<110:#back out of room
        backwards()
    stop()
    turnLeft()#face left
    while front.calcDistance()<95:#back out of hallway
        backwards()
    turnLeft()
    while front.calcDistance()>23:#facing south in middle hallway
        forwards()
    turnRight()
    while front.calcDistance()>65:#move forward a bit into room3
        forwards()
    scanRoom3()
    if flame==False:
        killmovement()
    turnRight()
    turnRight()#turn 180 degrees
    while front.calcDistance()>61:#facing east moving towards room 4. should be in middle of room
        forwards()
    scanRoom4()
    if flame==False:
        killmovement()
    while front.calcDistance()>23:#facing east moving towards rightmost wall
        forwards()
    turnLeft()
    while front.calcDistance()>23:# facing north moving towards room 2
        forwards()
    turnLeft()
    while front.calcDistnace()>90:#facing west moving towards entrance of room1
        forwards()
    turnLeft()
    while front.calcDistance()>45:#move a bit into room1 
        forwards()
    scanRoom1()
    if flame==False:
        killmovement()
def position2():#starts after looking south on right most hallway
    turnRight()
    while front.calcDistance()>23:
        forwards()
    turnLeft()
    position1()#runs all the rooms for position1: 2,3,4. should find candle before going to room1
def position3():#starts after looking south on right most hallway
    position2()
def forwards():
def backwards():
def turnLeft():
def turnRight():
def stop():
def scanRoom1():
def scanRoom2():
def scanRoom3():
def scanRoom4():#robot starst from center of room on x axis
def stabilize():
    if left.calcDistance()<10:
        #insert code for slight right turn
    if right.calcDistance()<10:
        #insert code for slight left turn
def killmovement():#basically a very prolonged stop()

def main():
    if front.calcDistance()<50:
        #Dog in front, facing right
        #dog in position 1
        dogPos=1
        position1() #runs hardcode for dog at position 1

    elif left.calcDistance()<10:
        #Facing right, no dog in front
        #first check 51x70 room
        while(front.calcDistance()>69):
            forwards();
        stop()
        turnRight()
        while front.calcDistance()>45:#going a little bit into the room
            forwards()
        stop()
        scanRoom1()
        if flame==False:
            killmovement()
        while front.calcDistance()<74:#back out of first room
            backwards()
        stop()
        turnLeft()
        while front.calcDistance()>26:#heading east towards rightmost wall
            forwards()
        turnRight()
        if frontcalcDistance()<100:#looking south, checks if dog is in that hallway
            dogPos=2
            position2()#runs hardcode for dog at position 2
        else:
            dogPos=3
            position3()#runs hardcode for dog at position 3
        
    else:
        turnLeft()
        if front.calcDistance()<50:
            dogPos=1
            position1()
        else:##same code as above
            #Facing right, no dog in front
            #first check 51x70 room
            while(front.calcDistance()>69):
                forwards();
            stop()
            turnRight()
            while front.calcDistance()>45:#going a little bit into the room
                forwards()
            stop()
            scanRoom1()
            if flame==False:
                killmovement()
            while front.calcDistance()<74:#back out of first room
                backwards()
            stop()
            turnLeft()
            while front.calcDistance()>26:#heading east towards rightmost wall
                forawrds()
            turnRight()
            if frontcalcDistance()<100:#looking south, checks if dog is in that hallway
                dogPos=2
                position2()#runs hardcode for dog at position 2
            else:
                dogPos=3
                position3()#runs hardcode for dog at position 3
main()
