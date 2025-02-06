import cv2 as cv
import numpy as np

img = cv.imread('resources/warp2.jpg')
height,width = img.shape[:2]
points = []
def onClick(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:
        points.append([x,y])
        cv.putText(img,'('+str(x)+','+str(y)+')',(x,y),cv.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),1)
        
cv.namedWindow('Image')
while True:
    cv.imshow('Image',img)
    cv.setMouseCallback('Image',onClick)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
print(points)
pts1 = np.array(points,dtype=np.float32) 
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv.getPerspectiveTransform(pts1,pts2)
output = cv.warpPerspective(img,matrix,(width,height))
cv.imshow('Output',output)
cv.waitKey(0)
cv.destroyAllWindows()