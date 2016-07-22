import numpy as np
import cv2
drawing = False  # True if mouse id is pressed
mode = True # draw rectancle else draw circle
ix, iy = -1,-1
img = np.zeros((500,500,3),np.uint8)

def draw_me(event,x,y,flags,param):
    global drawing, ix, iy, mode  #if not defined,then:=   UnboundLocalError: local variable 'drawing' referenced before assignment

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix = x
        iy = y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:        
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(255,0,0),3)
            else:
                cv2.circle(img,(x,y),4,(0,255,0),-1) 

    if event == cv2.EVENT_LBUTTONUP:
        drawing = False
        ###########################
        #I don't know what these lines are doing here             
        if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(255,0,0),3)
            else:
                cv2.circle(img,(x,y),4,(0,255,0),-1) 
        ###########################

cv2.namedWindow("image")
cv2.setMouseCallback("image",draw_me)

while(1):
    cv2.imshow("image",img)
    k = cv2.waitKey(1) & 0xff
    if k == ord("m"):
        mode = not mode
    if k == 27:
        break
cv2.destroyAllWindows()

        
