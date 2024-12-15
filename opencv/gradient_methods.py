import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('resources/hand.jpg',0)
lap = cv.Laplacian(img,cv.CV_64F,ksize=3)
lap = np.uint8(np.absolute(lap))
sobelX = cv.Sobel(img,cv.CV_64F,1,0,ksize=3)
sobelY = cv.Sobel(img,cv.CV_64F,0,1,ksize=3)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

titles = ['original','Laplacian','SobelX','SobelY']
images = [img,lap,sobelX,sobelY]

for i in range(len(images)):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.axis('off')
    
plt.show()

cv.destroyAllWindows()