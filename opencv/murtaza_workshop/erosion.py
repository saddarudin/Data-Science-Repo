import cv2 as cv
import numpy as np

img = cv.imread('resources/dog.jpg')

blur_img = cv.GaussianBlur(img,(7,7),0)

canny = cv.Canny(blur_img,100,100)

kernel = np.ones((5,5),np.uint8)
dilated = cv.dilate(canny,kernel,iterations=2)
erroded = cv.erode(dilated,kernel,iterations=2)

cv.imshow('canny image',canny)
cv.imshow('dilated image',dilated)
cv.imshow('erroded image',erroded)
cv.waitKey(0)
cv.destroyAllWindows()