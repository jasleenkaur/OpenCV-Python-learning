#http://stackoverflow.com/questions/34712144/merge-hsv-channels-under-opencv-3-in-python
#this program seprate hue from hsv images and show it
import cv2

image = cv2.imread('images/sample1.jpg')
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv_image)
s.fill(255) # fill saturation =255
v.fill(255)  # fill value =255
#only hue is left original
hsv_image = cv2.merge([h, s, v])   #merge 3 channels i.e h,s,v

out = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)  #convert to bgr

cv2.imshow('example', hsv_image)
cv2.waitKey(0)
