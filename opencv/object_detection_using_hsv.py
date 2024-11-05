import numpy as np
import cv2 as cv

img = cv.imread('resources/balls.jpg')
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

cv.imshow('original image',img)
cv.waitKey(0)
cv.destroyAllWindows()