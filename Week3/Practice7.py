# Image Blurring

import cv2

img = cv2.imread('img/sst-foyer.jpg')

cv2.imshow('Original Image', img)
cv2.waitKey(0)

# Gaussian Blur
gaussian = cv2.GaussianBlur(img, (7, 7), 0)
cv2.imshow('Gaussian Blurring', gaussian)
cv2.waitKey(0)

# Median Blur
median = cv2.medianBlur(img, 5)
cv2.imshow('Median Blurring', median)
cv2.waitKey(0)

# Bilateral Blur
bilateral = cv2.bilateralFilter(img, 9, 75, 75)
cv2.imshow('Bilateral Blurring', bilateral)
cv2.waitKey(0)

cv2.destroyAllWindows()