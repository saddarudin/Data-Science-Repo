import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Histogram is a graphical representation of the intensity distribution of an image
img = cv.imread('resources/dog.jpg',0)
# part1

# img = np.zeros((200,200),np.uint8)
# cv.rectangle(img,(0,100),(200,200),(255),-1)
# cv.rectangle(img,(0,50),(100,100),(127),-1)

# part2


# b, g, r = cv.split(img)
# plt.hist(img.ravel(),256,[0,256],color='gray')
# plt.hist(b.ravel(),256,[0,256],color='b')
# plt.hist(g.ravel(),256,[0,256],color='g')
# plt.hist(r.ravel(),256,[0,256],color='r')
# plt.xlabel('Intensity Value')
# plt.ylabel('Pixels Count')
# cv.imshow('Image',img)
# cv.imshow('Blue',b)
# cv.imshow('Green',g)
# cv.imshow('Red',r)
# plt.show()

# part3


hist = cv.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist)
cv.imshow('Image',img)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()