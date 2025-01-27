import cv2 as cv
import numpy as np

ones = np.ones((300,300,3),'uint8')*255
cv.imshow('original image',ones)
blue = ones.copy()
# assigning blue color
blue[:,:]=(255,0,0) 
cv.imshow('blue image',blue)

cv.waitKey(0)
cv.destroyAllWindows()