#Image Reflection

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('img/sst-foyer.jpg', 0)

# plot original image
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(img)

rows, cols = img.shape
M = np.float32([[1, 0, 0], [0, -1, rows], [0, 0, 1]])
reflected_img = cv.warpPerspective(img, M, (int(cols), int(rows)))

# plot reflected image
plt.subplot(1, 2, 2)
plt.title("Reflected Image")
plt.imshow(reflected_img)
plt.show()

cv.imwrite('img/reflected_out.jpg', reflected_img)
cv.waitKey(0)
cv.destroyAllWindows()
