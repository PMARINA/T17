# import the necessary packages
from imutils import contours
#from skimage import measure
import numpy as np
import argparse
import imutils
import cv2

class Detect_Color:
    def __init__(self,inputimage):
        self.inputimage=image
        self.image = cv2.imread(inputimage)
        self.boundaries = [([220, 220, 220], [255, 255, 255])]
        for (lower, upper) in boundaries:
            lower = np.array(lower, dtype = "uint8")
            upper = np.array(upper, dtype = "uint8")
            mask = cv2.inRange(self.image, lower, upper)
            self.output = cv2.bitwise_and(self.image, self.image, mask=mask)
        
    def isFlame(self, black_max_bgr=(40, 40, 40)):
        # use this if you want to check channels are all basically equal
        # I split this up into small steps to find out where your error is coming from
        mean_bgr_float = np.mean(self.output, axis=(0,1))
        mean_bgr_rounded = np.round(mean_bgr_float)
        mean_bgr = mean_bgr_rounded.astype(np.uint8)
        # use this if you just want a simple threshold for simple grayscale
        # or if you want to use an HSV (V) measurement as in your example
        mean_intensity = int(round(np.mean(self.output)))
        return False if np.all(mean_bgr < black_max_bgr) else True        

    def leftright(self):
        coord = np.where(np.all(self.output == (255, 255, 255), axis=-1))
        print (zip (coord[0], coord[1]))

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
