import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load an color image in grayscale
img = cv2.imread('images/bugs.jpg', 0)  # 0 for grayscale
'''cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27: #ESC key is pressed
    cv2.destroyAllWindows()
elif k == ord('s'):  #s for save
    cv2.imwrite('images/000.png',img)
    cv2.destroyAllWindows()
'''
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
