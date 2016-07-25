#program demonstrates thresholding of hue image is better than threshholding gray scale image
import cv2
import numpy as np
import argparse

# Construct argument parse to inline image with command
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())
 
# load the image
img = cv2.imread(args["image"])

hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
res1 = np.hstack((img,hsv_image)) 

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray_hsv = cv2.cvtColor(hsv_image,cv2.COLOR_BGR2GRAY)
res2 = np.hstack((gray,gray_hsv)) 

ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret, thresh_hsv = cv2.threshold(gray_hsv,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
res3 = np.hstack((thresh,thresh_hsv))
cv2.imwrite("res1.jpg",res1)
cv2.imwrite("res2.jpg",res2)
cv2.imwrite("res3.jpg",res3)
cv2.waitKey(0)
