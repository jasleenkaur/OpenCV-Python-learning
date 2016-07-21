import numpy as np
import cv2

im = cv2.imread('images/sample1.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
can = cv2.Canny(imgray, 75, 200)
#ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy = cv2.findContours(can,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow("thresh",can)
cv2.imshow("image", im)
cv2.imshow("image", imgray)
cv2.waitKey(0)
