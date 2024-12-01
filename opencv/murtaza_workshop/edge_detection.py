import cv2 as cv

img = cv.imread('resources/dog.jpg')

blur_img = cv.GaussianBlur(img,(7,7),0)

canny = cv.Canny(blur_img,100,100)

cv.imshow('original image',img)
cv.imshow('blur image',blur_img)
cv.imshow('canny image',canny)
cv.waitKey(0)
cv.destroyAllWindows()