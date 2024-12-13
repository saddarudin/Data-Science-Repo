import cv2 as cv

img = cv.imread('resources/colours.jpg',0)

ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)

cv.imshow('original',img)
cv.imshow('thresh1',thresh1)
cv.imshow('thresh2',thresh2)
cv.imshow('thresh3',thresh3)
cv.imshow('thresh4',thresh4)
cv.imshow('thresh5',thresh5)

cv.waitKey(0)
cv.destroyAllWindows()