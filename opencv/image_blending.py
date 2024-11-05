### Image blending means adding two images
### For blending two images they should be of same size
### Two functions are used add and addWeighted

import cv2 as cv
import numpy as np


img1 = cv.imread('resources/faces.jpg')
img2 = cv.imread('resources/faces2.jpg')
img1 = cv.resize(img1,(500,600))
img2 = cv.resize(img2,(500,600))
cv.imshow('original faces1',img1)
cv.imshow('original faces2',img2)

result1 = cv.add(img1,img2)
result2 = cv.addWeighted(img1,0.7,img2,0.3,0)

cv.imshow('result1',result1)
cv.imshow('result2',result2)

cv.waitKey(0)
cv.destroyAllWindows()