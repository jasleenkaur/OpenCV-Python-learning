# blobs counting
import cv2
import numpy as np
'''img = cv2.imread("images/sample1.jpg", cv2.IMREAD_GRAYSCALE)
ret,thresh = cv2.threshold(img,127,255,0)
edged = cv2.Canny(img, 75, 200)
img=edged
'''
img = cv2.imread("images/sample3.jpg",0)
#ret,thresh = cv2.threshold(img,127,255,0)
#b,g,r= cv2.split(img)
ret,th1 = cv2.threshold(img,120,255,cv2.THRESH_BINARY)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)

'''
#median = cv2.medianBlur(th1,5) #not working in this case
#gauss = cv2.GaussianBlur(th1,(5,5),1)
#blur = cv2.bilateralFilter(th1,9,75,75)
#gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
#contours,hierarchy = cv2.findContours(img,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
'''
#ret,th1 = cv2.threshold(img,120,255,cv2.THRESH_BINARY)
_, contours, _= cv2.findContours(th1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
idx =0 
for cnt in contours:
    idx += 1
    x,y,w,h = cv2.boundingRect(cnt)
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
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
cv2.imshow("keypoints",img)
cv2.imshow("thresh",th1)
cv2.imshow("erosion",erosion)
cv2.waitKey(0)

