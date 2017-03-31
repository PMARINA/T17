# import the necessary packages
from imutils import contours
#from skimage import measure
import numpy as np
import argparse
import imutils
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())
 
# load the image
image = cv2.imread(args["image"])

# define the list of boundaries
boundaries = [([220, 220, 220], [255, 255, 255])]

# loop over the boundaries
#change
for (lower, upper) in boundaries:
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
 
	# find the colors within the specified boundaries and apply
	# the mask
    mask = cv2.inRange(image, lower, upper)
    thresh = cv2.threshold(mask, 200, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=4)
    output = cv2.bitwise_and(image, image, thresh = thresh)
 
        # show the images
    cv2.imshow("images", np.hstack([output]))
    cv2.waitKey(0)
