import cv2
import os
import matplotlib.pyplot as plt
import numpy as np

def login():
    print("\nWelcome to Image Enhancement X")
    print("------------------------------")
    print("Provide your login details\n")

    while True:
        Username = input("Please input your username: ")
        Matno = input("Please input your Matric Number: ")
        print("\n")

        filename = generate_filename(Username, Matno)

        if os.path.exists(filename):
            print("Welcome, " + Username + "!")
            print("Your image was found!")
            print("------------------------------\n")
            return Username, Matno
        else:
            print("!!! Invalid Username or Password. No image found. \nPlease try again.\n")
            login()

def generate_filename(Username, Matno):
    return "img/" + Username + "_" + Matno + ".jpg"

def list_operations():
    print("Operations")
    print("----------")
    print("1. Add a suprise to your Image")
    print("2. Adjust Brightness & Contrast of your Image")
    print("3. Color Inversion")
    print("4. Image Scaling")
    print("5. Gray Scale Conversion")
    print("6. Noise Removal")
    print("7. Image Sharpening")
    print("8. Exit")

def add_default_image(image):
    default = cv2.imread('img/default.jpg')

    image = cv2.resize(image, (500, 400))
    default = cv2.resize(default, (500, 400))

    addImage = cv2.addWeighted(image, 0.5, default, 0.6, 0)

    cv2.imshow('Weighted Image', addImage)

    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()

def adjust_brightness_contrast(image):
    plt.subplot(1, 2, 1)
    plt.title("Original")
    plt.imshow(image)

    brightness = 5 
    contrast  = 1.5
    image1 = cv2.addWeighted(image, contrast, np.zeros(image.shape, image.dtype), 0, brightness)

    plt.subplot(1, 2, 2)
    plt.title("Brightness & Contrast")
    plt.imshow(image1)
    plt.show()

def color_inversion(image):
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(image)

    inverse_image = 255 - image

    plt.subplot(1, 2, 2)
    plt.title("Inverse Color")
    plt.imshow(inverse_image)

    plt.show()

def image_scaling(image):
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(image)

    scaled_image = cv2.resize(image, None, fx=2, fy=2)

    plt.subplot(1, 2, 2)
    plt.title("Scaled Image")
    plt.imshow(scaled_image)

    plt.show()

def gray_scale_conversion(image):
    pass

def noise_removal(image):
    plt.subplot(1, 2, 1)
    plt.title("Original")
    plt.imshow(image)

    filtered_image = cv2.medianBlur(image, 15)

    plt.subplot(1, 2, 2)
    plt.title("Median Blur")
    plt.imshow(filtered_image)

    plt.show()

def image_sharpening(image):
    plt.subplot(1, 2, 1)
    plt.title("Original")
    plt.imshow(image)

    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

    sharpened_image = cv2.filter2D(image, -1, kernel)

    plt.subplot(1, 2, 2)
    plt.title("Sharpening")
    plt.imshow(sharpened_image)
    plt.show()

def save_image(image):
    choice = input("Do you want to save your enhanced image? (y/n): ")

    if choice.lower() == 'y':
        cv2.imwrite('img/Enhanced_Image.jpg', image)
        print("Image saved successfully")
    else:
        print("Image not saved")

def exit_program():
    exit()


def main():
    # print("Welcome to the Image Enhancement Program!")
    username, matno = login()
    print(f"Logged in as {username} with Matric Number {matno}.\n")

    filename = generate_filename(username, matno)

    operations = {
        '1' : add_default_image,
        '2' : adjust_brightness_contrast,
        '3' : color_inversion,
        '4' : image_scaling,
        '5' : gray_scale_conversion,
        '6' : noise_removal,
        '7' : image_sharpening,
        '8' : exit_program
    }

    image = cv2.imread(filename)
    if image is None:
        print("Error: Image not found.")
        exit()

    list_operations()
    operation = input("Please select an operation to perform: ")

    if operation in operations:
        operations[operation](image)
    else:
        print("Invalid operation. Please enter a valid operation number")


main()




