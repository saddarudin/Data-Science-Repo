import cv2 as cv

img = cv.imread('murtaza_workshop/shah 58 Challan.png')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow('image',gray)
cv.waitKey(0)
cv.destroyAllwindows()