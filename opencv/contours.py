# Contours are used for shape analysis, object detection or object recognition, etc.

import cv2 as cv

img = cv.imread('resources/OpenCV.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,thresh = cv.threshold(gray,200,255,0)
contours,heirarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
print(f'Number of contours: {len(contours)}')
print(contours[0])
cv.drawContours(img,contours,-1,(0,255,0),3)

cv.imshow('Original Image',img)
cv.imshow('Gray Image',gray)
cv.imshow('Threshold Image',thresh)

cv.waitKey(0)
cv.destroyAllWindows()