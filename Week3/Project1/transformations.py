import os
import cv2
import numpy as np

def list_operations():
    print("\nTransformation Options:")
    print("1. Image Translation")
    print("2. Image Reflection")
    print("3. Image Rotation")
    print("4. Image Cropping")
    print("5. Image Blurring")
    print("6. Image Shearing in X-axis")
    print("7. Image Shearing in Y-axis")
    print("8. Exit")

def image_translation(image, artwork_name):
    print("Performing Image Translation")
    rows, cols, _ = image.shape

    M = np.float32([[1, 0, 50], [0, 1, 50]])
    translated_image = cv2.warpAffine(image, M, (cols, rows))

    cv2.imshow("Translated Image", translated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    save_option = input("\nWould you like to save the translated image? (yes/no): ")
    if save_option.lower() == 'yes':
        save_image(translated_image, "translated_image", artwork_name, "translated")

def image_reflection(image, artwork_name):
    print("Performing Image Reflection")
    rows, cols, _ = image.shape

    M = np.float32([[1, 0, 0], [0, -1, rows], [0, 0, 1]])
    reflected_image = cv2.warpPerspective(image, M, (int(cols), int(rows)))

    cv2.imshow("Reflected Image", reflected_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    save_option = input("\nWould you like to save the reflected image? (yes/no): ")
    if save_option.lower() == 'yes':
        save_image(reflected_image, "reflected_image", artwork_name, "reflected")

def image_rotation(image, artwork_name):
    print("Performing Image Rotation")
    rows, cols, _ = image.shape

    rotated_image = cv2.warpAffine(image, cv2.getRotationMatrix2D((cols/2, rows/2), 30, 0.6), (cols, rows))

    cv2.imshow("Rotated Image", rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    save_option = input("\nWould you like to save the rotated image? (yes/no): ")
    if save_option.lower() == 'yes':
        save_image(rotated_image, "rotated_image", artwork_name, "rotated")

def image_cropping(image, artwork_name):
    print("Performing Image Cropping")

    cropped_image = image[450:700, 200:500]

    cv2.imshow("Cropped Image", cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    save_option = input("\nWould you like to save the cropped image? (yes/no): ")
    if save_option.lower() == 'yes':
        save_image(cropped_image, "cropped_image", artwork_name, "cropped")

def image_blurring(image, artwork_name):
    print("Performing Image Blurring")
    cv2.imshow('Original Image', image)
    cv2.waitKey(0)

    # Gaussian Blur
    gaussian = cv2.GaussianBlur(image, (7, 7), 0)
    cv2.imshow('Gaussian Blurring', gaussian)
    cv2.waitKey(0)

    # Median Blur
    median = cv2.medianBlur(image, 5)
    cv2.imshow('Median Blurring', median)
    cv2.waitKey(0)

    # Bilateral Blur
    bilateral = cv2.bilateralFilter(image, 9, 75, 75)
    cv2.imshow('Bilateral Blurring', bilateral)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

    save_option = input("\nWould you like to save the blurred image? (yes/no): ")
    if save_option.lower() == 'yes':
        save_image(bilateral, "blurred_image", artwork_name, "blurred")

def image_shearing_in_X_axis(image, artwork_name):
    print("Performing Image Shearing in X-axis")
    rows, cols, _ = image.shape

    M = np.float32([[1, 0.5, 0], [0, 1, 0], [0, 0, 1]])
    sheared_image = cv2.warpPerspective(image, M, (int(cols*1.5), int(rows*1.5)))

    cv2.imshow("Sheared Image in X-axis", sheared_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    save_option = input("\nWould you like to save the sheared image in X-axis? (yes/no): ")
    if save_option.lower() == 'yes':
        save_image(sheared_image, "sheared_X_image", artwork_name, "sheared_X")

def image_shearing_in_Y_axis(image, artwork_name):
    print("Performing Image Shearing in Y-axis")
    rows, cols, _ = image.shape

    M = np.float32([[1, 0, 0], [0.5, 1, 0], [0, 0, 1]])
    sheared_image = cv2.warpPerspective(image, M, (int(cols*1.5), int(rows*1.5)))

    cv2.imshow("Sheared Image in Y-axis", sheared_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    save_option = input("\nWould you like to save the sheared image in Y-axis? (yes/no): ")
    if save_option.lower() == 'yes':
        save_image(sheared_image, "sheared_Y_image", artwork_name, "sheared_Y")

def save_image(image, filename, artwork_name, transformation_name):
    if not os.path.exists('img'):
        os.makedirs('img')
    
    filename = os.path.join('img', f"{artwork_name}_{transformation_name}.jpg")
    cv2.imwrite(filename, image)
    print(f"Transformed image saved as '{filename}'")

def exit_program(image):
    print("Exiting Program")

def main(image, artwork_name):   
    operations = {
        '1': image_translation,
        '2': image_reflection,
        '3': image_rotation,
        '4': image_cropping,
        '5': image_blurring,
        '6': image_shearing_in_X_axis,
        '7': image_shearing_in_Y_axis,
        '8': exit_program
    }
    
    list_operations()
    operation = input("Please select an operation to perform: ")

    if operation in operations:
        operations[operation](image, artwork_name)
    else:
        print("Invalid operation. Please enter a valid operation number")
