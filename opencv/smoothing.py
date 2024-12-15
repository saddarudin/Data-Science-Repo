import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('resources/Noise_salt_and_pepper.png',0)
img = cv.cvtColor(img,cv.COLOR_BGR2RGB) #for displaying in matplotlib
# formula for kernel is 1/(k_width*k_height)*np.ones((k_width,k_height))
kernel = np.ones((5,5),np.float32)/25
dst = cv.filter2D(img,-1,kernel)
blur = cv.blur(img,(5,5))
gblur = cv.GaussianBlur(img,(5,5),0)
# median filter is specially used for salt and pepper noise
median = cv.medianBlur(img,3)
bilateral = cv.bilateralFilter(img,9,75,75)

titles = ['Original','2D Convolutional','Blur','G Blur','Median','Bilateral']
images = [img,dst,blur,gblur,median,bilateral]

for i in range(len(images)):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.axis('off')
    
    
plt.show()

cv.destroyAllWindows()