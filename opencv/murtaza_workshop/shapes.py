import cv2 as cv
import numpy as np

img = np.zeros((512,512,3),np.uint8)


# converting into white image
img[:]=255,255,255

# drawing lines
j = 20
for i in range(0,24):
    cv.line(img,(0,j),(512,j),(0,0,0),3)
    j = j + 20
cv.imshow('black image',img)

cv.waitKey(0)
cv.destroyAllWindows()