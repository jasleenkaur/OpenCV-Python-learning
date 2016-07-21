import cv2
import numpy as np

img = cv2.imread("images/sample1.jpg")
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray_hsv = cv2.cvtColor(hsv,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret, thresh_hsv = cv2.threshold(gray_hsv,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#CV_THRESH_BINARY_INV
########################################################
 #noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh_hsv,cv2.MORPH_OPEN,kernel, iterations = 2)

# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=1)
opening[:]= 255-opening[:]

'''
# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
# Marker labelling
ret, markers = cv2.connectedComponents(sure_fg)

# Add one to all labels so that sure background is not 0, but 1
markers = markers+1

# Now, mark the region of unknown with zero
markers[unknown==255] = 0
markers = cv2.watershed(img,markers)
img[markers == -1] = [255,0,0]
'''
cv2.imshow('opening',opening)
cv2.imshow('sure_bg',sure_bg)
cv2.imwrite('images/sure_bg.png',sure_bg)

########################################################

#cv2.imshow('orginal',thresh)
#cv2.imshow('hsv',thresh_hsv)
cv2.waitKey(0)
