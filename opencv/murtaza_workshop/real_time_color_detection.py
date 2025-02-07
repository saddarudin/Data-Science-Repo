import cv2 as cv
import numpy as np

cap = cv.VideoCapture('http://10.11.17.250:8080/video')
width,height = 640,480
cap.set(3,width)
cap.set(4,height)

def doNothing(x):
    pass


cv.namedWindow('hsv')
cv.resizeWindow('hsv',640,240)
cv.createTrackbar('hmin','hsv',0,179,doNothing)
cv.createTrackbar('hmax','hsv',179,179,doNothing)
cv.createTrackbar('smin','hsv',0,255,doNothing)
cv.createTrackbar('smax','hsv',255,255,doNothing)
cv.createTrackbar('vmin','hsv',0,255,doNothing)
cv.createTrackbar('vmax','hsv',255,255,doNothing)


while cap.isOpened():
    ret,frame = cap.read()
    if ret:
        frame = cv.resize(frame,(width,height))
        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        hmin = cv.getTrackbarPos('hmin','hsv')
        hmax = cv.getTrackbarPos('hmax','hsv')
        smin = cv.getTrackbarPos('smin','hsv')
        smax = cv.getTrackbarPos('smax','hsv')
        vmin = cv.getTrackbarPos('vmin','hsv')
        vmax = cv.getTrackbarPos('vmax','hsv')
        lower = np.array([hmin,smin,vmin])
        upper = np.array([hmax,smax,vmax])
        mask = cv.inRange(hsv,lower,upper)
        result = cv.bitwise_and(frame,frame,mask=mask)
        cv.imshow('Mask',mask)
        cv.imshow('Result',result)
        cv.imshow('Original',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    

cap.release()
cv.destroyAllWindows()