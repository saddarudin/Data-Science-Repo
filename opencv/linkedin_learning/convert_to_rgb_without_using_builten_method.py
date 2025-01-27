import cv2 as cv
import numpy as np

ones = np.ones((300,300,3),'uint8')*255
bgr = ones.copy()
bgr[:,:]=(255,0,0)

b,g,r = cv.split(bgr)
rgb = cv.merge([r,g,b])

cv.imshow('bgr image',bgr)
cv.imshow('rgb image',rgb)
cv.waitKey(0)
cv.destroyAllWindows()