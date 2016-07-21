import cv2
import numpy as np

filename = raw_input()

I = cv2.imread(filename, 0)
I = cv2.medianBlur(I, 3)
bw = cv2.adaptiveThreshold(I, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 101, 1)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (17, 17))
bw = cv2.dilate(cv2.erode(bw, kernel), kernel)

print np.round_(np.sum(bw == 0) / 3015.0)
