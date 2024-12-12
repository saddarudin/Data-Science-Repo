import cv2 as cv

img = cv.imread('resources/balls.jpg')
b,g,r = cv.split(img)
cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('Red',r)
cv.imshow('original image',img)
cv.waitKey(0)
cv.destroyAllWindows()