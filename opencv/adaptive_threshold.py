import cv2 as cv

img = cv.imread('resources/colours.jpg',0)
# Simple thresholding
ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)

# Adaptive thresholding
thresh2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
thresh3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)

cv.imshow('original',img)
cv.imshow('thresh1',thresh1)
cv.imshow('thresh2',thresh2)
cv.imshow('thresh3',thresh3)

cv.waitKey(0)
cv.destroyAllWindows()
