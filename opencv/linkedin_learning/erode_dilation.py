import cv2 as cv
import numpy as np

img = cv.imread('resources/colours.jpg')
kernel = np.ones((3,3),'uint8')
erode = cv.erode(img,kernel,iterations=1)
dilate = cv.dilate(img,kernel,iterations=1)

cv.imshow('Original Image',img)
cv.imshow('Eroded Image',erode)
cv.imshow('Dilated Image',dilate)

cv.waitKey(0)
cv.destroyAllWindows()