# The Hough Transform is a populat technique to detect any shape, if you can represent that shape in a mathematical form.
# The most popular use of the Hough Transform is to detect lines in an image, but it can also be used to detect circles or other shapes.
# It can detect the shape even if it is broken or distorted a little bit.

# Hough Transformation Algorithm
# 1. Edge Detection. For example, using the Canny edge detector.
# 2. Mapping of edge points to the Hough space and storage in an accumulator.
# 3. Interpretation of the accumulator to yield lins of infinite length. 
#    The interpretation is done by thresholding and possibly other constraints.
# 4. Conversion of infinite lines to finite lines.


# Open CV implements two kinds of Hough Line Transforms:
# 1. The Standard Hough Transform (HoughLines method)
# 2. The Probabilistic Hough Line Transform (HoughLinesP method)

import cv2 as cv
import numpy as np

img = cv.imread('resources/sudoku.png')
img = cv.resize(img,(500,500))
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
edge = cv.Canny(gray,50,150,apertureSize=3)
lines = cv.HoughLines(edge,1,np.pi/180,200)

for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0+1000*(-b))
    y1 = int(y0+1000*a)
    x2 = int(x0-1000*(-b))
    y2 = int(y0-1000*a)
    cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)


cv.imshow('Original Image',img)
cv.waitKey(0)
cv.destroyAllWindows()