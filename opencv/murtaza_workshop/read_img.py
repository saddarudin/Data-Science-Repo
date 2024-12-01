import cv2 as cv

img = cv.imread('resources/dog.jpg')

cv.imshow('dog',img)

cv.waitKey(0)
cv.destroyAllWindows()
