import cv2 as cv

img = cv.imread('resources/dog.jpg')

blur_img = cv.GaussianBlur(img,(7,7),0)

cv.imshow('original image',img)
cv.imshow('blur image of dog',blur_img)

cv.waitKey(0)
cv.destroyAllWindows()