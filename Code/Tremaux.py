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
def sub_alg(steps):
