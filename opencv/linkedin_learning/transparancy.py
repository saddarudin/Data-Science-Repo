import cv2 as cv
import numpy as np

img = cv.imread('resources/dog.jpg')
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]
not_green_transparant = cv.merge((b,g,r,r))
cv.imwrite("resources/dog.png",not_green_transparant)