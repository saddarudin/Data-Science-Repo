import numpy as np
import cv2 as cv

img1 = np.zeros((500,500,3),np.uint8)
img1 = cv.rectangle(img1, (50,100),(200,170),(255,255,255),-1)

img2 = np.zeros((500,500,3),np.uint8)
img2 = cv.rectangle(img2,(300,30),(200,170),(255,255,255),-1)
bitAnd = cv.bitwise_and(img1,img2)
bitOR = cv.bitwise_or(img1,img2)
img1Not = cv.bitwise_not(img1)
img2Not = cv.bitwise_not(img2)
bitXOR = cv.bitwise_xor(img1,img2)
cv.imshow('image1',img1)
cv.imshow('image2',img2)
cv.imshow('bitAnd',bitAnd)
cv.imshow('bitOR',bitOR)
cv.imshow('img1Not',img1Not)
cv.imshow('img2Not',img2Not)
cv.imshow('bitXOR',bitXOR)
cv.waitKey(0)
cv.destroyAllWindows()