import cv2 as cv 
import numpy as np

img = cv.imread('resources/sdb.jpg')

cv.namedWindow('trackbars')

def nothing(x):
    pass


hue_min = cv.createTrackbar('hue min','trackbars',0,179,nothing)
hue_max = cv.createTrackbar('hue max','trackbars',179,179,nothing)
sat_min = cv.createTrackbar('sat min','trackbars',0,255,nothing)
sat_max = cv.createTrackbar('sat max','trackbars',255,255,nothing)
val_min = cv.createTrackbar('val min','trackbars',0,255,nothing)
val_max = cv.createTrackbar('val max','trackbars',255,255,nothing)

while True:
    hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    h_min = cv.getTrackbarPos('hue min','trackbars')
    h_max = cv.getTrackbarPos('hue max','trackbars')    
    s_min = cv.getTrackbarPos('sat min','trackbars')
    s_max = cv.getTrackbarPos('sat max','trackbars')
    v_min = cv.getTrackbarPos('val min','trackbars')
    v_max = cv.getTrackbarPos('val max','trackbars')
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv.inRange(hsv,lower,upper)  
    result = cv.bitwise_and(img,img,mask=mask)
    # cv.imshow('image',img)
    cv.imshow('mask',mask)
    cv.imshow('result',result)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()