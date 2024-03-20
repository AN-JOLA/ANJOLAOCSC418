#Inverse Transform

import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('img/sst-foyer.jpg')

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image)

inverse_image = 255 - image

cv2.imwrite('img/inverse_image.jpg', inverse_image)

plt.subplot(1, 2, 2)
plt.title("Inverse Color")
plt.imshow(inverse_image)

plt.show()