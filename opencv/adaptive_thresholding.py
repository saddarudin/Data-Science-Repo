## Simple thresholding is not able to handle different type of low luminance pixels
## Adaptive thersholding algorithm calculate the threshold value for a small region of the image
## So we get multiple threshold values for different regions of the same image
## Adaptive method decides how thresholding value is calculated

import cv2 as cv

img = cv.imread('resources/sdb.jpg',0)
thresh, binary = cv.threshold(img,127,255,cv.THRESH_BINARY)
adaptive_thresh_mean = cv.adaptiveThreshold(img, 255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
adaptive_thresh_gaussian = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
cv.imshow('original image',img)
cv.imshow('adaptive threshold image',adaptive_thresh_mean)
cv.imshow('adaptive threshold gaussian image',adaptive_thresh_gaussian)
cv.imshow('binary',binary)
cv.waitKey(0)
cv.destroyAllWindows()