import cv2
import numpy
import time
cap = cv2.VideoCapture(0)
#t = time.time()
while(cap.isOpened()):
    ret,frame = cap.read()
    frame = cv2.flip(frame,0)
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow("new image",gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
#t2 = time.time() -t
#print "time taken: " + str(t2)
cv2.destroyAllWindows()
