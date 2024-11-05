import numpy as np
import cv2 as cv

def nothing(x):
    pass

img = np.zeros((400,400,3),np.uint8)

cv.namedWindow('color picker',cv.WINDOW_NORMAL)

cv.createTrackbar('R','color picker',0,255,nothing)
cv.createTrackbar('G','color picker',0,255,nothing)
cv.createTrackbar('B','color picker',0,255,nothing)

while True:
    cv.imshow('color picker',img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    r = cv.getTrackbarPos('R','color picker')
    g = cv.getTrackbarPos('G','color picker')
    b = cv.getTrackbarPos('B','color picker')
    img[:]  = [b,g,r]   
cv.destroyAllWindows()