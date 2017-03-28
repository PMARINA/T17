def main(past_moves,steps):
    inmaze=True;
    while inmaze==True:
        #pastrightdist=currentrightdist
        #pastleftdist=currentleftdist
        #currentrightdist=rightsensor.getDistance()
        #currentleftdist=leftsensor.getDistance()
        #frontdist=frontsensor.getDistance()
        if past_moves[-1]=="forward":
            current
        junction = isAtJunction()
        if junction==True:
            marked = isPathMarked()
            if marked==True:
                sub_alg(steps)
            else:
                #go backwards
            #mark path
        else:
            sub_alg(steps)
        steps+=1
    
def isAtJunction():
    if abs(currentrightdist-lastrightdist)>5:
        return true
    else if abs(currentleftdist-lastleftdist)>5:
        return true
def isPathMarked():
    
def canGoForward():
def canGoRight():
def canGoLeft():
def turnLeft():
def turnRight():
def moveForward():
def moveBackward():

def sub_alg(steps):
    forward=canGoForward()
    if forward==True:
        #moving forward
        past_moves.append("forward")
        main(past_moves,steps)
    else:
        right=canGoRight()
        if right==True:
            #turn right
            past_moves.append("right")
            main(past_moves,steps)
        else:
            left=canGoLeft()
            if left==True:
                #turn left
                past_moves.append("left")
                main(past_moves,steps)
            else:
                #move backwards code here
                past_moves.append("backwards")
                main(past_moves,steps)
                

currentrightdist=0
currentleftdist=0
lastrightdist=0
lastleftdist=0
frontdist=0
currentx=0 #change start x
currenty=0 #change start y
#rightsensor=Sensor(trig echo here)
#leftsensor=Sensor(trig echo here)
#frontsensor=Sensor(trig echo here)
locationmap=[[0 for x in range(244)]for y in range(244)]
steps=0
past_moves=[]
main(past_moves,steps)
