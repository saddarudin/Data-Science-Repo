import cv2 as cv

img1 = cv.imread('resources/dog.jpg')
img2 = cv.imread('resources/dog_head.jpg')
img2 = cv.resize(img2,(100,100))
cv.namedWindow('image')
def image_placer(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:
        img1[y:y+img2.shape[0],x:x+img2.shape[1]] = img2
        cv.imshow('image',img1)

cv.imshow('image',img1)
cv.setMouseCallback('image',image_placer)
cv.waitKey(0)
cv.destroyAllWindows()