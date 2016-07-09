#FLIPPING BGR TO RGB
import cv2
#import numpy as np
import matplotlib.pyplot as plt
import time
t1=time.time()
img = cv2.imread('images/baby.jpg')
'''
b,g,r = cv2.split(img)
img2 = cv2.merge([r,g,b])
plt.subplot(121);plt.imshow(img) # expects distorted color
plt.subplot(122);plt.imshow(img2) # expect true color
plt.show()

cv2.namedWindow('bgr image', cv2.WINDOW_NORMAL)
cv2.namedWindow('rgb image', cv2.WINDOW_NORMAL)
cv2.imshow('bgr image',img) # expects true color
cv2.imshow('rgb image',img2) # expects distorted color
cv2.waitKey(0)
cv2.destroyAllWindows()
'''



'''
img2 = img[:,:,::-1]
plt.subplot(121);plt.imshow(img) # expects distorted color
plt.subplot(122);plt.imshow(img2) # expect true color
plt.show()

'''

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.subplot(121);plt.imshow(img) # expects distorted color
plt.subplot(122);plt.imshow(img2) # expect true color
plt.show()  #need to call show function of pyplot explicitly

t2 = time.time()-t1
print "time taken: " + str(t2)

