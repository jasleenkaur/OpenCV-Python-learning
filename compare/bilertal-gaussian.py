# bilateral filter blur image except edges and also outer noise gets enhance,  therefore gausian is consider best for this detecting bricks.
import cv2
import numpy as np
import argparse

# Construct argument parse to inline image with command
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())
 
# load the image
img = cv2.imread(args["image"])
# median filter gives bad result : 

#gaussain is beter in this case than median
blur = cv2.bilateralFilter(img,9,75,75)
# convert BGR TO HSV
hsv= cv2.cvtColor(blur ,cv2.COLOR_BGR2HSV)
gray_hsv = cv2.cvtColor(hsv,cv2.COLOR_BGR2GRAY)

# Otsu Thresholding
ret, thresh_hsv = cv2.threshold(gray_hsv,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("bilateral filter", thresh_hsv)

##########

blur = cv2.GaussianBlur(img,(9,9),10.0)
hsv= cv2.cvtColor(blur ,cv2.COLOR_BGR2HSV)
gray_hsv = cv2.cvtColor(hsv,cv2.COLOR_BGR2GRAY)

# Otsu Thresholding
ret, thresh_hsv = cv2.threshold(gray_hsv,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("gaussian filter", thresh_hsv)


cv2.waitKey(0)
