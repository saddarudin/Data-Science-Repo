import cv2 as cv

img = cv.imread('resources/dog.jpg')
img = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_CONSTANT,value=[255,0,0])
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()