# to detect perticular colored object. we need its hue + saturation. hue is a perticular color, say red. And saturation is presence amount of that colour.
import cv2
import numpy as np
import argparse

# Construct argument parse to inline image with command
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())
 
# load the image
img = cv2.imread(args["image"])
img1 = cv2.imread(args["image"])
#blur image with gaussian
blur = cv2.GaussianBlur(img,(9,9),10.0)

# convert BGR TO HSV
hsv = cv2.cvtColor(img ,cv2.COLOR_BGR2HSV)
h,s,v =cv2.split(hsv)

#cv2.imwrite("saturation",s)
cv2.imwrite("value.jpg",v)
h.fill(255)
v.fill(255)
hsv_image = cv2.merge([h, s, v])
cv2.imwrite("hsv.jpg", hsv)
cv2.imwrite("hsv_image.jpg", hsv_image)
out = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)


######
#bgr2hsv image
gray_hsv = cv2.cvtColor(hsv,cv2.COLOR_BGR2GRAY)
ret, thresh_hsv1 = cv2.threshold(gray_hsv,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite("th-hsv.jpg",thresh_hsv1)

####
#hsv_image after combining s-channel with altered v,h channel
gray_hsv = cv2.cvtColor(hsv_image,cv2.COLOR_BGR2GRAY)
ret, thresh_hsv2 = cv2.threshold(gray_hsv,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite("thresh-hsv_image.jpg", thresh_hsv2)
####

#original image
gray_hsv = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
ret, thresh_hsv4 = cv2.threshold(gray_hsv,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite("thresh-original_image.jpg", thresh_hsv4)
