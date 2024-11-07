import cv2 as cv
import numpy as np

img = cv.imread('resources/geometry.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray,5)

circles = cv.HoughCircles(gray,cv.HOUGH_GRADIENT,1,170,param1=50,param2=30,minRadius=0,maxRadius=0)
data = np.uint16(np.around(circles))
print(data)
for (x,y,r) in data[0,:]:
    cv.circle(img,(x,y),r,(0,255,0),2)
    cv.circle(img,(x,y),2,(0,0,255),3)
cv.imshow('gray',gray)
cv.imshow('detected circles',img)
cv.waitKey(0)
cv.destroyAllWindows()