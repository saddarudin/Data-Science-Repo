from utilities import stackImages
import cv2 as cv


img = cv.imread('resources/shapes.jpg')
contoursImage = img.copy()
grayImage = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
_,thresh = cv.threshold(grayImage,220,255,cv.THRESH_BINARY)

contours,hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
print(len(contours))
for cnt in contours:
    area = cv.contourArea(cnt)
    cv.drawContours(contoursImage,cnt,-1,(0,255,0),3)
    peri = cv.arcLength(cnt,True)
    approx = cv.approxPolyDP(cnt,0.02*peri,True)
    x,y,w,h = cv.boundingRect(approx)
    cv.rectangle(contoursImage,(x,y),(x+w,y+h),(255,0,0),3)
stackedImages = stackImages(0.5,([img,grayImage],[thresh,contoursImage]))
cv.imshow('Stacked Images',stackedImages)
cv.waitKey(0)
cv.destroyAllWindows()