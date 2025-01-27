import cv2 as cv

img = cv.imread('resources/dog.jpg')
blur = cv.GaussianBlur(img,(5,5),0)
cv.imshow('Original Image',img)
cv.imshow('Gaussian Blur',blur)
cv.waitKey(0)
cv.destroyAllWindows()