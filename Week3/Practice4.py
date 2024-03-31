#Image Cropping

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('img/sst-foyer.jpg', 0)

# plot original image
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(img)

cropped_img = img[450:700, 200:500]

# plot cropped image
plt.subplot(1, 2, 2)
plt.title("Cropped Image")
plt.imshow(cropped_img)

cv.imwrite('img/cropped_out.jpg', cropped_img)
plt.show()