import cv2 as cv

img1 = cv.imread('resources/faces.jpg')
img2 = cv.imread('resources/faces2.jpg')
img1 = cv.resize(img1,(700,500))
img2 = cv.resize(img2,(700,500))

def nothing(x):
    pass

cv.namedWindow('image')
cv.createTrackbar('aplha','image',0,100,nothing)


while True:
    alpha = cv.getTrackbarPos('aplha','image')/100
    beta = 1-alpha
    result = cv.addWeighted(img1,alpha,img2,beta,0)
    cv.imshow('image',result)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()