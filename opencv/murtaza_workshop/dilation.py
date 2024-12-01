### Dilation increases the thickness of edges detected in canny image

import numpy as np
import cv2 as cv

img = cv.imread('resources/dog.jpg')

blur_img = cv.GaussianBlur(img,(7,7),0)

canny = cv.Canny(blur_img,100,100)

kernel = np.ones((5,5),np.uint8)
dilated = cv.dilate(canny,kernel,iterations=1)

cv.imshow('canny image',canny)
cv.imshow('dilated image',dilated)
cv.waitKey(0)
cv.destroyAllWindows()
