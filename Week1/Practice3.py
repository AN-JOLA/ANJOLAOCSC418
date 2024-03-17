import cv2
import os

img_path = r'C:\Users\ajayn\OneDrive\Documents\SCHOOL\COURSE_WORK\YEAR_4\SEMESTER_2\SPECIAL_TOPICS_IN_CS\ANJOLAOCSC418\img\crypto.jpg'

directory = r'C:\Users\ajayn\OneDrive\Documents\SCHOOL\COURSE_WORK\YEAR_4\SEMESTER_2\SPECIAL_TOPICS_IN_CS\ANJOLAOCSC418\img'

img = cv2.imread(img_path, 0)

os.chdir(directory)

print("Before saving image:")
print(os.listdir(directory))

filename = 'grayCryptoImg.jpg'

cv2.imwrite(filename, img)

print("After saving image:")
print(os.listdir(directory))

print('Successfully saved')