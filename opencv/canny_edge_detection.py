# It is composed of 5 steps:
# 1. Noise Reduction
# 2. Gradient Calculation
# 3. Non Maximum Suppression
# 4. Double Threshold
# 5. Edge Tracking by Hysteresis

import cv2 as cv

img = cv.imread('resources/hand.jpg',0)

cv.namedWindow('Canny')
def nothing(x):
    pass


thresh1 = cv.createTrackbar('Threshold1','Canny',0,255,nothing)
thresh2 = cv.createTrackbar('Threshold2','Canny',0,255,nothing)


while True:
    cv.imshow('Original',img)
    threshold1 = cv.getTrackbarPos('Threshold1','Canny')
    threshold2 = cv.getTrackbarPos('Threshold2','Canny')
    canny = cv.Canny(img,threshold1,threshold2)
    cv.imshow('Canny',canny)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()