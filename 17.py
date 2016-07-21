import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/sample3.jpg', cv2.IMREAD_GRAYSCALE)
gray = cv2.imread('images/sample3.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow("image",gray)
cv2.waitKey(0)
#img = cv2.medianBlur(img,5)

ret,th1 = cv2.threshold(img,120,255,cv2.THRESH_BINARY)

#median = cv2.medianBlur(th1,5) #not working in this case
gauss = cv2.GaussianBlur(th1,(5,5),1)
blur = cv2.bilateralFilter(th1,9,75,75)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
# Otsu's thresholding
ret2,th4 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Otsu's thresholding after Gaussian filtering
blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th5 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

titles = ['Original Image', 'Global Thresholding after median',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding', "OTSU Thresholding", "Otsu Thresholding after gaussian"]
images = [img, gauss, blur, th3, th4, th5]

for i in xrange(6):
    plt.subplot(3,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
