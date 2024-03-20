#Image Scaling

import cv2
import matplotlib.pyplot as plt

image = cv2.imread('img/sst.jpg')

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image)

scaled_image = cv2.resize(image, None, fx=2, fy=2)

cv2.imwrite('img/Scaled.jpg', scaled_image)

plt.subplot(1, 2, 2)
plt.title("Scaled Image")
plt.imshow(scaled_image)

plt.show()