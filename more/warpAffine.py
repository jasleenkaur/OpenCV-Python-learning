import cv2
import numpy as np

img = cv2.imread('images/baby.jpg')

res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

#OR
print img.shape
print img.shape[:2]
height, width = img.shape[:2]

rows,cols = img.shape[:2]

M = np.float32([[1,0,200],[0,1,200]])
trans = cv2.warpAffine(img,M,(cols,rows))

M = cv2.getRotationMatrix2D((cols,rows),90,1)
rot = cv2.warpAffine(img,M,(cols,rows))

res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)
cv2.namedWindow("trans",cv2.WINDOW_NORMAL)
cv2.namedWindow("rot",cv2.WINDOW_NORMAL)
cv2.imshow("trans", trans)
cv2.imshow("rot", rot)
cv2.waitKey(0)
