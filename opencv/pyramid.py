import cv2 as cv

# There are two methods for image pyramids:
# 1. Gaussian Pyramid
# 2. Laplacian Pyramid

img = cv.imread('resources/hand.jpg')
p1 = cv.pyrDown(img)
p2 = cv.pyrDown(p1)
p3 = cv.pyrUp(p2)
p4 = cv.pyrUp(p3)

cv.imshow('Original',img)
cv.imshow('PyrDown1',p1)
cv.imshow('PyrDown2',p2)
cv.imshow('PyrUp1',p3)
cv.imshow('PyrUp2',p4)
cv.waitKey(0)
cv.destroyAllWindows()