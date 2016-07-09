import numpy as np
import cv2

img = np.zeros((512,512,3), np.uint8)
img[:,0:150]=255
img[:,151:300]=(255,0,0)
img[0:300,300:511]=111

    
img=cv2.line(img,(0,0),(511,511),(255,0,0),5,cv2.LINE_AA)
img=cv2.rectangle(img,(200,200),(400,400),(0,0,255))
img=cv2.circle(img, (300,300),50,(0,255,0))
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,(0,0,255),-1)
cv2.namedWindow("image",cv2.WINDOW_NORMAL)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
