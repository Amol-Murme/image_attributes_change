import cv2
import numpy as np

image = cv2.imread('images/cat1.jfif')
cv2.imshow('befor',image)
kernel = np.array([[-1,-1,-1],[-1, 10,-1],[-1,-1,-1]])
sharpened = cv2.filter2D(image, -1, kernel) # applying the sharpening kernel to the input image & displaying it.
cv2.imshow('Image Sharpening', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()