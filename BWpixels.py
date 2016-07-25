import cv2
import numpy as np
import argparse

# Construct argument parse to inline image with command
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())
 
# load the image
img = cv2.imread(args["image"])
#blur image with gaussian
blur = cv2.GaussianBlur(img,(9,9),10.0)

# convert BGR TO HSV
hsv = cv2.cvtColor(img ,cv2.COLOR_BGR2HSV)

gray_hsv = cv2.cvtColor(hsv,cv2.COLOR_BGR2GRAY)
# Otsu Thresholding
ret, thresh_hsv1 = cv2.threshold(gray_hsv,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

white = np.count_nonzero(thresh_hsv);
rows,cols,channel = img.shape
totalpixels = rows *cols
black = totalpixels - white
print "count_white: " + str(white)
print "black_pixels" + str(black)
