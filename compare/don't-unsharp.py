import cv2
import numpy as np
import argparse

# Construct argument parse to inline image with command
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())
 
# load the image
img = cv2.imread(args["image"])
# median filter gives bad result : 

#unsharp masking
#gaussain is beter in this case than median
blur = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow("gaussain",blur)


#gaussian_3 = cv2.GaussianBlur(img, (9,9), 10.0)
#unsharp_image = cv2.addWeighted(img, 1.5, gaussian_3, -0.5, 0, img)

# convert BGR TO HSV
hsv= cv2.cvtColor(blur ,cv2.COLOR_BGR2HSV)
#cv2.imshow("gray level of image", hsv[1])

gray_hsv = cv2.cvtColor(hsv,cv2.COLOR_BGR2GRAY)

# Otsu Thresholding

ret, thresh_hsv = cv2.threshold(gray_hsv,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("thresh.jpg", thresh_hsv)
####

blur = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow("gaussain",blur)


#gaussian_3 = cv2.GaussianBlur(img, (9,9), 10.0)
unsharp_image = cv2.addWeighted(img, 1.5, blur, -0.5, 0, img)

# convert BGR TO HSV
hsv= cv2.cvtColor(unsharp_image ,cv2.COLOR_BGR2HSV)
#cv2.imshow("gray level of image", hsv[1])

gray_hsv = cv2.cvtColor(hsv,cv2.COLOR_BGR2GRAY)

# Otsu Thresholding

ret, thresh_hsv_unsharp = cv2.threshold(gray_hsv,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("thresh-unsharp.jpg", thresh_hsv_unsharp)



