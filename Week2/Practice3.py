#Adjusting Brightness & Contrast of an Image

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('img/sst.jpg')

plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(image)

brightness = 5 
contrast  = 1.5
image2 = cv2.addWeighted(image, contrast, np.zeros(image.shape, image.dtype), 0, brightness)


cv2.imwrite('img/contrast_image.jpg', image2)

plt.subplot(1, 2, 2)
plt.title("Brightness & Contrast")
plt.imshow(image2)
plt.show()