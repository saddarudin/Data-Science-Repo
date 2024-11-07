import cv2 as cv
import numpy as np

img = cv.imread('resources/sdb.jpg')
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rectangle = (100,80,386,596)
mask = np.zeros(img.shape[:2],np.uint8)
cv.grabCut(img,mask,rectangle,bgdModel,fgdModel,5,cv.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1,).astype('uint8')
img = img*mask2[:,:,np.newaxis]
cv.imshow('my image',img)
cv.waitKey(0)
cv.destroyAllWindows()