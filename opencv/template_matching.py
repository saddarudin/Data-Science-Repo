import cv2 as cv
import numpy as np

img = cv.imread('resources/faces.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
template = cv.imread('resources/template.jpg',0)
h,w = template.shape
result = cv.matchTemplate(gray,template,cv.TM_CCOEFF_NORMED)
threshold = 0.99
loc = np.where(result>=threshold)

for pt in zip(*loc[::-1]):
    cv.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,0,255),2)

cv.imshow('Original',img)
cv.imshow('Template',template)
cv.waitKey(0)
cv.destroyAllWindows()