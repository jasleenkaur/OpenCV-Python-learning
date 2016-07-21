# blobs counting
import cv2
import numpy as np
img = cv2.imread("images/bricks.png",0)
#gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#ret,thresh = cv2.threshold(img,0, 255, cv2.THRESH_OTSU);
#edged = cv2.Canny(img, 75, 200)
image, contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

idx =0 
for cnt in contours:
    idx += 1
    x,y,w,h = cv2.boundingRect(cnt)
    brick = cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)   
# roi=img[y:y+h,x:x+w]
   # cv2.imwrite("out/"+str(idx) + '.jpg', roi)
    #cv2.rectangle(im,(x,y),(x+w,y+h),(200,0,0),2)

'''
img = cv2.imread("images/bricks.png", cv2.IMREAD_GRAYSCALE)

#set up detector with default value
detector = cv2.SimpleBlobDetector_create()

#detect blobs
keypoints = detector.detect(img)
  
#draw detecd blobs as red circles
im_key = cv2.drawKeypoints(img, keypoints, np.array([]),(0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
'''
print "total number of bricks: " + str(idx)
cv2.imshow("keypoints",image)
cv2.waitKey(0)
