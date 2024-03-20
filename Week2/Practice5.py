# Removing Noise

import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('img/sst-foyer.jpg')

plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(image)

#Removing noise using median filter
filtered_image = cv2.medianBlur(image, 15)

cv2.imwrite('img/Median-Blur.jpg', filtered_image)

plt.subplot(1, 2, 2)
plt.title("Median Blur")
plt.imshow(filtered_image)

plt.show()