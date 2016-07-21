import cv2
import numpy as np

img = cv2.imread("images/sample1.jpg")
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# calculating object histogram
roihist = cv2.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )

# normalize histogram and apply backprojection
#dst=cv2.normalize(roihist,roihist,0,255,cv2.NORM_MINMAX)
#dst = cv2.calcBackProject([hsvt],[0,1],roihist,[0,180,0,256],1)

# Now convolute with circular disc
#disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
#cv2.filter2D(dst,-1,disc,dst)

# threshold and binary AND
ret,thresh = cv2.threshold(hsv,172,255,0)
#thresh = cv2.merge((thresh,thresh,thresh))

cv2.imshow('img',img)
cv2.imshow('hsv',hsv)
#cv2.imshow('dst',dst)
cv2.imshow('thresh',thresh)
cv2.waitKey(0)
