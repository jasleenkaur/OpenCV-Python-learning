import cv2

cap = cv2.VideoCapture(0)
fourcc= cv2.VideoWriter_fourcc(*'MJPG')
out= cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
while(cap.isOpened()):
    ret,frame = cap.read()
    out.write(frame)
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow("new image",gray)
    if (cv2.waitKey(1) & 0xFF ==ord(q)):
        break
cap.release()
out.release()
cv2.destroyAllWindows()
