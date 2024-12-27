import cv2 as cv
import numpy as np

img = cv.imread('resources/shapes.jpg')
img = cv.resize(img,(500,500))
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

corners = cv.goodFeaturesToTrack(gray,50,0.01,10)
corners = np.int0(corners)

for corner in corners:
    x,y = corner.ravel()
    cv.circle(img,(x,y),3,255,-1)
    
cv.imshow('Chess Board',img)
cv.waitKey(0)
cv.destroyAllWindows()