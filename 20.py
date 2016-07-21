import cv2
import numpy as np
img = cv2.imread("images/sample3.jpg",0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
#ret,thresh = cv2.threshold(img,127,255,0)
#b,g,r= cv2.split(img)
cv2.imshow("keypoints",erosion)
cv2.waitKey(0)
