import cv2 as cv
import numpy as np


def stackImages(scale,imageArray):
    rows = len(imageArray)
    cols = len(imageArray[0])
    
    rowsAvailable = isinstance(imageArray[0],list)
    
    width = imageArray[0][0].shape[1]
    height = imageArray[0][0].shape[0]
    
    if rowsAvailable:
        for x in range(0,rows):
            for y in range (0,cols):
                if imageArray[x][y].shape[:2] == imageArray[0][0].shape[:2]:
                    imageArray[x][y] = cv.resize(imageArray[x][y],(0,0),None,scale,scale)
                else:
                    imageArray[x][y] = cv.resize(imageArray[x][y],(imageArray[0][0].shape[1],imageArray[0][0].shape[0]),None,scale,scale)
                if len(imageArray[x][y].shape) == 2: imageArray[x][y]= cv.cvtColor(imageArray[x][y], cv.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height,width,3),np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        
        for x in range(0,rows):
            hor[x] = np.hstack(imageArray[x])
            
        ver = np.vstack(hor)
    else:
        for x in range(0,rows):
            if imageArray[x].shape[:2] == imageArray[0].shape[:2]:
                imageArray[x] = cv.resize(imageArray[x],(0,0),None,scale,scale)
            else:
                imageArray[x] = cv.resize(imageArray[x],(imageArray[0].shape[1],imageArray[0].shape[0]),None,scale,scale)
            if len(imageArray[x].shape) == 2: imageArray[x]= cv.cvtColor(imageArray[x], cv.COLOR_GRAY2BGR)
        
        hor = np.hstack(imageArray)
        ver = hor
    return ver


frameWidth = 640
frameHeight = 480

cap = cv.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

while True:
    success,img = cap.read()
    cv.imshow('Video',img)
    
    kernel = np.ones((5,5),np.uint8)
    
    imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)    
    imgBlur = cv.GaussianBlur(imgGray,(7,7),0)
    imgCanny = cv.Canny(imgBlur,100,200)
    imgDialation = cv.dilate(imgCanny,kernel,iterations=2)
    imgEroded = cv.erode(imgDialation,kernel,iterations=1)
    
    stackedImages = stackImages((0.3),
                                ([img,imgGray,imgBlur,imgCanny,imgDialation,imgEroded],
                                [img,imgGray,imgBlur,imgCanny,imgDialation,imgEroded],
                                [img,imgGray,imgBlur,imgCanny,imgDialation,imgEroded]))
    cv.imshow('Staked Images',stackedImages)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()