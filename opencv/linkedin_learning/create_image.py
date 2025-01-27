import numpy as np
import cv2 as cv

zeros = np.zeros((500,500,1),'uint8')
ones = np.ones((300,300,1),'uint8')*255
cv.imshow('black',zeros)
cv.imshow('white',ones)
cv.waitKey(0)
cv.destroyAllWindows()