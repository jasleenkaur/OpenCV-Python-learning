import cv2
import numpy as np

img = cv2.imread('images/bugs.jpg')
print img.shape
copy=img[80:250,200:300]
img[280:450,150:250]=copy
while(1):
    cv2.imshow("image", img)
    if cv2.waitKey(0):
        break
