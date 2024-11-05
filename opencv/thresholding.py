import cv2 as cv

img = cv.imread('resources/sdb.jpg',0)
thresh,binary = cv.threshold(img,127,255,cv.THRESH_BINARY)
thresh,binary_inv = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
thresh,binary_trunc = cv.threshold(img,127,255,cv.THRESH_TRUNC)
# truncate is a thresholding technique that sets the pixel value to the threshold value 
# if the pixel value is greater than the threshold value
thresh,binary_to_zero = cv.threshold(img,127,255,cv.THRESH_TOZERO)
cv.imshow('to zero image',binary_to_zero)
cv.waitKey(0)
cv.destroyAllWindows()
