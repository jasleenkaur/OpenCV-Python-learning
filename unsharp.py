import cv2
#http://stackoverflow.com/questions/32454613/python-unsharp-mask
image = cv2.imread("images/sample11.jpg")
gaussian_3 = cv2.GaussianBlur(image, (9,9), 10.0)
unsharp_image = cv2.addWeighted(image, 1.5, gaussian_3, -0.5, 0, image)
cv2.imwrite("lenna_unsharp.jpg", unsharp_image)
