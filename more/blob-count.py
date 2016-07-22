#!/usr/bin/python

# Standard imports
import cv2
import numpy as np;
from matplotlib import pyplot as plt

# Read image
im = cv2.imread("images/sure_bg.png")

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params(im)


#Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
	detector = cv2.SimpleBlobDetector(params)
else : 
	detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs.
keypoints = detector.detect(im)
print len(keypoints)
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob

im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (255,0,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("keypts",im_with_keypoints)
cv2.waitKey(0)
