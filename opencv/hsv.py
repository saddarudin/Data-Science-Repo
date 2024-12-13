# HSV ==> Hue Saturation Value
# Hue corresponds to color components(base pigment), hence just by selecting a range of Hue (0-360) you can select any color.
# Saturation is the amount of color (depth of the pigment)(dominance of Hue)(0-100%)
# Value is basically the brightness of the color(0-100%)

import cv2 as cv
import numpy as np

img = cv.imread('resources/colours.jpg')

def nothing(x):
    pass


cv.namedWindow('image')
lh = cv.createTrackbar('lh','image',0,255,nothing)
uh = cv.createTrackbar('uh','image',255,255,nothing)
ls = cv.createTrackbar('ls','image',0,255,nothing)
us = cv.createTrackbar('us','image',255,255,nothing)
lv = cv.createTrackbar('lv','image',0,255,nothing)
uv = cv.createTrackbar('uv','image',255,255,nothing)


while True:
    frame = cv.imread('resources/colours.jpg')
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    lh = cv.getTrackbarPos('lh','image')
    uh = cv.getTrackbarPos('uh','image')
    ls = cv.getTrackbarPos('ls','image')
    us = cv.getTrackbarPos('us','image')
    lv = cv.getTrackbarPos('lv','image')
    uv = cv.getTrackbarPos('uv','image')
    
    lower_bound = np.array([lh,ls,lv])
    upper_bound = np.array([uh,us,uv])
    
    mask = cv.inRange(hsv,lower_bound,upper_bound)
    res = cv.bitwise_and(frame,frame,mask=mask)
    
    cv.imshow('original',frame)
    cv.imshow('mask',mask)
    cv.imshow('result',res)
    
    if cv.waitKey(1) & 0xFF==ord('q'):
        break
    
cv.destroyAllWindows()
    
