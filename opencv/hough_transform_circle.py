import cv2 as cv
import numpy as np

img = cv.imread('resources/geometry.jpg')
output = np.copy(img)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur = cv.medianBlur(gray,5)
circles = cv.HoughCircles(blur,cv.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
detected_circles = np.uint16(np.around(circles))

for (x,y,r) in detected_circles[0,:]:
    cv.circle(output,(x,y),r,(0,255,0),3)
    cv.circle(output,(x,y),2,(0,255,255),3)

cv.imshow('Image',output)
cv.waitKey(0)
cv.destroyAllWindows()