# Harris Corner Detection Steps:
# 1. Determine which windows produce very large variations in intensity when moved in both X and Y directions.
# 2. With each such window found, a score R is computed.
# 3. After applying a threshold to this score, important corners are selected and marked.

# 1. If mod(R) is small then the region is flat
# 2. If R < 0 then the region is an edge
# 3. If R is large then the region is a corner

import cv2 as cv
import numpy as np

img = cv.imread('resources/chess.jpg')
img = cv.resize(img,(500,500))
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray = np.float32(gray)

dst = cv.cornerHarris(gray,2,3,0.04)
ds = cv.dilate(dst,None)
img[dst>0.01*dst.max()] = [0,0,255]

cv.imshow('Chess Board',img)
cv.waitKey(0)
cv.destroyAllWindows()