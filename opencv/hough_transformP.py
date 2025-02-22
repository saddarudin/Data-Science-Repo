import cv2 as cv
import numpy as np

img = cv.imread('resources/sudoku.png')
img = cv.resize(img,(500,500))
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
edge = cv.Canny(gray,50,150,apertureSize=3)
lines = cv.HoughLinesP(edge,1,np.pi/180,100,minLineLength=100,maxLineGap=10)

for line in lines:
    x1,y1,x2,y2 = line[0]
    cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)


cv.imshow('Original Image',img)
cv.waitKey(0)
cv.destroyAllWindows()