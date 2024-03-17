import cv2

path = 'img/crypto.jpg'

img = cv2.imread(path, 0)

window_name = 'Display Image'

cv2.imshow(window_name, img)

cv2.waitKey(0)

cv2.destroyAllWindows()