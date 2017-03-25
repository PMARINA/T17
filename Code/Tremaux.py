def main(past_moves,steps):
    inmaze=True;
    while inmaze=True:
        junction = isAtJunction()
        if junction==True:
            marked = isPathMarked()
            if marked==True:
                sub_alg(steps)
            else:
                #go backwards
        else:
            sub_alg(steps)
        steps+=1
    
def isAtJunction():
def isPathMarked():
def canGoForward():
def canGoRight():
def canGoLeft():
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
                


steps=0
past_moves=[]
main(past_moves,steps)
