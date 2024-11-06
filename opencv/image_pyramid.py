import cv2 as cv

img = cv.imread('resources/dog.jpg')
# Gaussian Pyramid has two methods: pyrDown and pyrUp
down1 = cv.pyrDown(img)
down2 = cv.pyrDown(down1)

up1 = cv.pyrUp(down2)
up2 = cv.pyrUp(up1)
cv.imshow('Original Image', img)
cv.imshow('Down 1', down1)
cv.imshow('Down 2', down2)
cv.imshow('Up 1',up1)
cv.imshow('Up 2',up2)

cv.waitKey(0)
cv.destroyAllWindows()