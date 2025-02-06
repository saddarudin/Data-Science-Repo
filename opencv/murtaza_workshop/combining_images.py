from utilities import stackImages
import cv2 as cv

img1 = cv.imread('resources/apple.jpg')
img2 = cv.imread('resources/balls.jpg')
img3 = cv.imread('resources/blue.jpg')
img4 = cv.imread('resources/chess.jpg')
img5 = cv.imread('resources/colours.jpg')
img6 = cv.imread('resources/dog.jpg')


imgStack = stackImages(0.5,[[img1,img2,img3],[img4,img5,img6]])

cv.imshow('Stacked Images',imgStack)
cv.waitKey(0)
cv.destroyAllWindows()