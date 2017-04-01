# import the necessary packages
from imutils import contours
#from skimage import measure
import numpy as np
import argparse
import imutils
import cv2

class Detect_Color:
    def __init__(self,inputimage):
        self.inputimage=inputimage
        self.image = cv2.imread(inputimage)
        self.boundaries = [([220, 220, 220], [255, 255, 255])]
        for (lower, upper) in self.boundaries:
            lower = np.array(lower, dtype = "uint8")
            upper = np.array(upper, dtype = "uint8")
            mask = cv2.inRange(self.image, lower, upper)
            self.output = cv2.bitwise_and(self.image, self.image, mask=mask)
        
    def isFlame(self,black_max_bgr=(1, 1, 1)):
        
        # use this if you want to check channels are all basically equal
        # I split this up into small steps to find out where your error is coming from
        mean_bgr_float = np.mean(self.output, axis=(0,1))
        mean_bgr_rounded = np.round(mean_bgr_float)
        mean_bgr = mean_bgr_rounded.astype(np.uint8)
        # use this if you just want a simple threshold for simple grayscale
        # or if you want to use an HSV (V) measurement as in your example
        mean_intensity = int(round(np.mean(self.output)))
        return False if np.all(mean_bgr < black_max_bgr) else True        

    #def leftright(self):
     #   coord = np.where(np.all(self.output == (255, 255, 255),axis=-1))
      #  print ( (coord[0], coord[1]))
    def leftright(self):
        imgray = cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(imgray,127,255,0)
        im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        #contours = cv2.findContours(thresh,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(self.output,contours,-1,(0,255,0),3)
        #contours=contours[0] if imutils.is_cv2() else contours[1]
        #c=max(contours,key=cv2.contourArea)
            # determine the most extreme points along the contour

            #these are x y values
##        extLeft = tuple(c[c[:, :, 0].argmin()][0]) 
##        extRight = tuple(c[c[:, :, 0].argmax()][0])
##        extTop = tuple(c[c[:, :, 1].argmin()][0])
##        extBot = tuple(c[c[:, :, 1].argmax()][0])

        #extLeft = tuple(c[c[0].argmin()][0]) 
        #extRight = tuple(c[c[0].argmax()][0])
        #extTop = tuple(c[c[1].argmin()][0])
        #extBot = tuple(c[c[1].argmax()][0])

        #centerx = (extLeft[0]+extRight[0])/2
        #centery = (extTop[1]+extBot[1])/2

        print(len(contours))
        print(contours)
        print(contours[0])
        print(contours[1])
        #cv2.imshow("images",self.output)
        #cv2.waitKey(0)


#6bC6N
# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", help = "path to the image")
#args = vars(ap.parse_args())
 
# load the image
# image = cv2.imread(args["image"])

# define the list of boundaries
#boundaries = [([220, 220, 220], [255, 255, 255])]

# loop over the boundaries
#change
    
#for (lower, upper) in boundaries:
    # create NumPy arrays from the boundaries
  #  lower = np.array(lower, dtype = "uint8")
 #   upper = np.array(upper, dtype = "uint8")
     
	# find the colors within the specified boundaries and apply
	# the mask
    #mask = cv2.inRange(image, lower, upper)
   # thresh = cv2.threshold(mask, 220, 255, cv2.THRESH_BINARY)[1]
    #thresh = cv2.erode(thresh, None, iterations=2)
    #thresh = cv2.dilate(thresh, None, iterations=4)
    #labels = measure.label(thresh, neighbors=8, background=0)
    #mask1 = np.zeros(thresh.shape, dtype="uint8")
    #output = cv2.bitwise_and(image, image, mask=mask)
 
        # show the images
    #cv2.imshow("images", output)
    #cv2.waitKey(0)
