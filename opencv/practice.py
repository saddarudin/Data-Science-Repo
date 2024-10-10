import cv2 as cv

img = cv.imread('resources/dog.jpg')

img1 = cv.resize(img,(600,600))

gray = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)

cv.imshow('image',gray)

cv.waitKey(0)
cv.destroyAllWindows()
