import cv2 as cv

img1 = cv.imread('resources/geometry.jpg')
img2 = cv.imread('resources/warp.png')

img1 = cv.resize(img1,(320,320))
img2 = cv.resize(img2,(320,320))


img3 = cv.add(img1,img2)
img4 = cv.addWeighted(img1,0.3,img2,0.7,0)

cv.imshow('Image1',img1)
cv.imshow('Image2',img2)
cv.imshow('Added Image',img3)
cv.waitKey(0)
cv.destroyAllWindows()