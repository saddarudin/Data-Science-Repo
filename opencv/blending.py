import cv2 as cv
import numpy as np

apple = cv.imread('resources/apple.jpg')
orange = cv.imread('resources/orange.jpg')

apple = cv.resize(apple,(512,512))
orange = cv.resize(orange,(512,512))

# blending through horizontal stacking
half_apple = apple[:, :256]
half_orange = orange[:,256:]
apple_orange = np.hstack((half_apple,half_orange))

# For image blending we need to follow the following steps:
# 1. Load the images
# 2. Find Gaussian Pyramid (say 6 levels)
# 3. From Gaussian Pyramid, find its Laplacian Pyramid
# 4. Now join the left half of one image and right half of other image in each levels of Laplacian Pyramids
# 5. Finally from this joint image pyramids, reconstruct the original image.


# Generating Gaussian Pyramid for Apple
apple_copy = apple.copy()
gp_apple = [apple_copy]

for i in range(6):
    apple_copy = cv.pyrDown(apple_copy)
    gp_apple.append(apple_copy)
    
# Generating Gaussian Pyramid for Orange
orange_copy = orange.copy()
gp_orange = [orange_copy]

for i in range(6):
    orange_copy = cv.pyrDown(orange_copy)
    gp_orange.append(orange_copy)
    
    
# Generating Laplacian Pyramid for Apple
apple_copy = gp_apple[5]
lp_apple = [apple_copy]

for i in range(5,0,-1):
    gaussian_extended = cv.pyrUp(gp_apple[i])
    laplacian = cv.subtract(gp_apple[i-1],gaussian_extended)
    lp_apple.append(laplacian)

# Generating Laplacian Pyramid for Orange

orange_copy =gp_orange[5]
lp_orange = [orange_copy]

for i in range(5,0,-1):
    gaussian_extended = cv.pyrUp(gp_orange[i])
    laplacian = cv.subtract(gp_orange[i-1],gaussian_extended)
    lp_orange.append(laplacian)
    
    
# Now add left and right halves of images in each level
apple_orange_pyramid = []
n = 0

for apple_lap,orange_lap in zip(lp_apple,lp_orange):
    n += 1
    cols,rows,ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[:,:int(cols/2):],orange_lap[:,int(cols/2):]))
    apple_orange_pyramid.append(laplacian)
    

# Reconstructing the image
apple_orange_reconstruct = apple_orange_pyramid[0]

for i in range(1,6):
    apple_orange_reconstruct = cv.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv.add(apple_orange_pyramid[i],apple_orange_reconstruct)
    

cv.imshow('Apple',apple)
cv.imshow('Orange',orange)
cv.imshow('Direct Blending',apple_orange)
cv.imshow('Blended Image',apple_orange_reconstruct)

cv.waitKey(0)
cv.destroyAllWindows()