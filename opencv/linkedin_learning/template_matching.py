import cv2 as cv
import numpy as np

img = cv.imread('resources/faces.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
template = cv.imread('resources/template.jpg',0)

result = cv.matchTemplate(gray,template,cv.TM_CCOEFF_NORMED)
h,w = template.shape
min_val,max_val,min_loc,max_loc = cv.minMaxLoc(result)
cv.rectangle(img,max_loc,(max_loc[0]+w,max_loc[1]+h),(0,0,255),2)
cv.imshow('Detected Image',img)
cv.imshow('template',template)
cv.imshow('Matching Result',result)
cv.waitKey(0)
cv.destroyAllWindows()
