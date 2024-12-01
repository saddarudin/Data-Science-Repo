import cv2 as cv

img = cv.imread('resources/dog.jpg')

width,height = 400,400

img= cv.resize(img,(width,height))

cv.imshow('dog image',img)
cv.waitKey(0)
cv.destroyAllWindows()

