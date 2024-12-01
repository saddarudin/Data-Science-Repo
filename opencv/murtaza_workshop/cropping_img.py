import cv2 as cv

img = cv.imread('resources/dog.jpg')

imgCropped = img[:,0:300]
print(img.shape)
cv.imshow('dog',img)
cv.imshow('cropped dog',imgCropped)
cv.waitKey(0)
cv.destroyAllWindows()