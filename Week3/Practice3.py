# Image Rotation

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('img/sst-foyer.jpg', 0)
rows, cols = img.shape

# plot original image
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(img)

img_rotation = cv.warpAffine(img, cv.getRotationMatrix2D((cols/2, rows/2), 30, 0.6), (cols, rows))                                                            

# plot rotated image
plt.subplot(1, 2, 2)
plt.title("Rotated Image")
plt.imshow(img_rotation)

cv.imshow('Rotated Image', img_rotation)
plt.title("Rotated Image")
cv.waitKey(0)
cv.destroyAllWindows()