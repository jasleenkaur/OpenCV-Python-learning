import cv2
import numpy as np
import argparse

# Construct argument parse to inline image with command
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())
 
# load the image
img = cv2.imread(args["image"])
#gaussain is beter in this case than median in this case
blur = cv2.GaussianBlur(img,(5,5),0)
# convert BGR TO HSV
hsv= cv2.cvtColor(blur ,cv2.COLOR_BGR2HSV)
gray_hsv = cv2.cvtColor(hsv,cv2.COLOR_BGR2GRAY)
# Otsu Thresholding
ret, thresh_hsv_gauss = cv2.threshold(gray_hsv,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("gaussain",blur)
cv2.imshow("thresh_hsv_gauss",thresh_hsv_gauss)
###########

median = cv2.medianBlur(img,5)
cv2.imshow("median", median)
hsv= cv2.cvtColor(median ,cv2.COLOR_BGR2HSV)
gray_hsv = cv2.cvtColor(hsv,cv2.COLOR_BGR2GRAY)

# Otsu Thresholding
ret, thresh_hsv_med = cv2.threshold(gray_hsv,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("median",median)
cv2.imshow("thresh_hsv_med",thresh_hsv_med)
cv2.waitKey(0)
