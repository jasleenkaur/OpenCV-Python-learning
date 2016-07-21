# blobs extraxt as seprate images  http://stackoverflow.com/questions/21104664/extract-all-bounding-boxes-using-opencv-python
import cv2
import numpy as np
img = cv2.imread("images/bricks.png", cv2.IMREAD_GRAYSCALE)
#gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
#contours,hierarchy = cv2.findContours(img,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

_, contours, _= cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
idx =0 
for cnt in contours:
    idx += 1
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('Features', img)
   # roi=img[y:y+h,x:x+w]
    #cv2.imwrite(str(idx) + '.jpg', roi)
    #cv2.rectangle(im,(x,y),(x+w,y+h),(200,0,0),2)

'''img = cv2.imread("images/bricks.png", cv2.IMREAD_GRAYSCALE)

#set up detector with default value
detector = cv2.SimpleBlobDetector_create()

#detect blobs
keypoints = detector.detect(img)
  
#draw detecd blobs as red circles
im_key = cv2.drawKeypoints(img, keypoints, np.array([]),(0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
'''
#cv2.imshow("keypoints",img)
cv2.waitKey(1)
