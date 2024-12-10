import cv2 as cv
import numpy as np
img = np.ones((512,512,3),np.uint8)
cv.line(img,(0,30),(512,30),(255,0,0),3)
cv.imshow('Image',img)
cv.waitKey(0)
cv.destroyAllWindows()