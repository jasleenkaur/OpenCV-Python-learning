# Standard imports
import cv2
import numpy as np;

# Read image
im = cv2.imread("images/blob.jpg", cv2.IMREAD_GRAYSCALE)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()
params.filterByColor = True
params.blobColor = 0
params.filterByArea = True;         # filter my blobs by area of blob
#params.minArea = 40;  
params.filterByCircularity = False
# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
	detector = cv2.SimpleBlobDetector(params)
else : 
	detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs.
keypoints = detector.detect(im)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, (0,255,0,))


# Show keypoints
cv2.imshow("image",im)
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)

