# Sheared Image in Y-Axis

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('img/sst-foyer.jpg', 0)
rows, cols = img.shape

# plot original image
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(img)

M = np.float32([[1, 0, 0], [0.5, 1, 0], [0, 0, 1]])
sheared_img = cv.warpPerspective(img, M, (int(cols*1.5), int(rows*1.5)))

plt.subplot(1, 2, 2)
plt.title("Sheared Image in Y-Axis")
plt.imshow(sheared_img)

plt.show()