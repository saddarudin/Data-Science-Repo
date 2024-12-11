import cv2 as cv
import numpy as np

def mouse_event(event,x,y,flags,param):
    if event==cv.EVENT_LBUTTONDOWN:
       cv.circle(img,(x,y),3,(0,255,0),-1)
       points.append((x,y))
       cv.imshow('Image',img)
       if len(points)>=2:
           cv.line(img,points[-2],points[-1],(255,0,0),2)
           cv.imshow('Image',img) 
    

img = np.ones((400,400,3),np.uint8)*255
points = []
cv.imshow('Image',img)
cv.setMouseCallback('Image',mouse_event)
cv.waitKey(0)
cv.destroyAllWindows()