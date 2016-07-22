#program to find best contrast method
import cv2
import numpy as np
import argparse

# Construct argument parse to inline image with command
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

# load the image
img = cv2.imread(args["image"])
##############################################################################3
#histogram equalisation
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
equ = cv2.equalizeHist(gray)
res1 = np.hstack((gray,equ)) #stacking images side-by-side

## create a CLAHE object (Arguments are optional).############# more good
clahe = cv2.createCLAHE(clipLimit=50, tileGridSize=(8,8))
cl1 = clahe.apply(gray)
res2 = np.hstack((gray,cl1)) #stacking images side-by-side

#unsharp masking
gaussian_3 = cv2.GaussianBlur(img, (9,9), 10.0)
unsharp_image = cv2.addWeighted(img, 1.5, gaussian_3, -0.5, 0, img)
res3 = np.hstack((img,unsharp_image)) #stacking images side-by-side

#
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

# equalize the histogram of the Y channel
img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])

# convert the YUV image back to RGB format
img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2RGB)

res4 = np.hstack((img,img_yuv,img_output)) #stacking images side-by-side


####
ret, thresh = cv2.threshold(equ,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret, thresh_yuv = cv2.threshold(img_output,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

################################################################################33
#display
cv2.imshow("thresh",thresh)
cv2.imshow("thresh_yuv",thresh_yuv)
cv2.imshow("hist_equ",res1)
cv2.imshow("CLAHE",res2)
cv2.imshow("unsharp_masking", res3)
cv2.imshow("color hist equ", res4)
cv2.imwrite("res4.jpg",res4)

cv2.waitKey(0)
