import cv2 as cv

img = cv.imread('resources/sdb.jpg')
b,g,r = cv.split(img)
cv.imshow('original image',img)
cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('Red',r)
img2 = cv.merge([b,g,r])
cv.imshow('merged image',img2)
cv.waitKey(0)
cv.destroyAllWindows()