import re
import cv2
import numpy as np
import requests

import artwork_data as ad
import transformations as it

def main():
    print("Welcome to the Yemisi Shyllon Museum of Art!")
    access_images()

def access_images():
    while True:
        email, age = get_user_info()
        
        categories = list(ad.art_collections.keys())
        display_categories(categories)
        
        category = get_user_category(categories)
        artworks = ad.art_collections[category]
        
        display_artworks(artworks, category)
        
        img, artwork_name = display_image(artworks)
        
        while True:
            transform_option = input("\nWould you like to transform the image? (yes/no): ")
            if transform_option.lower() == 'yes':
                it.main(img, artwork_name)
            else:
                break  # Exit the transformation loop if user doesn't want another transformation
        
        another_image_option = input("\nWould you like to view another image? (yes/no): ")
        if another_image_option.lower() != 'yes':
            break  # Exit the main loop if user doesn't want to view another image

def get_user_info():
    while True:
        email = input("Enter your email address ending with @pau.edu.ng: ")
        if not validate_email(email):
            print("Invalid email format. Please enter a valid email.")
            continue
        
        age = input("Enter your age: ")
        if not check_age(age):
            print("Invalid age. Please enter an age above 18.")
            continue
        age = int(age)
        
        return email, age

def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@pau\.edu\.ng$"
    return re.match(pattern, email) is not None

def check_age(age):
    return age.isdigit() and int(age) > 18

def display_categories(categories):
    print("\nSelect a category by entering a number:")
    for index, category in enumerate(categories, 1):
        print(f"{index}. {category}")

def get_user_category(categories):
    while True:
        category_number = input("Enter the number corresponding to the desired category: ")
        if not category_number.isdigit() or not (1 <= int(category_number) <= len(categories)):
            print("Invalid category number. Please enter a valid category number.")
            continue
        
        return categories[int(category_number) - 1]

def display_artworks(artworks, category):
    print(f"\nArtworks in the {category} category:")
    for index, (artwork_name, _) in enumerate(artworks.items(), 1):
        print(f"{index}. {artwork_name}")

def display_image(artworks):
    artwork_number = input("\nEnter the number corresponding to the desired artwork to view its image: ")
    if not artwork_number.isdigit() or not (1 <= int(artwork_number) <= len(artworks)):
        print("Invalid artwork number. Please enter a valid artwork number.")
        return None, None

    artwork_name, artwork_url = list(artworks.items())[int(artwork_number) - 1]
    response = requests.get(artwork_url)
    
    if response.status_code != 200:
        print(f"Error fetching image: {response.status_code}")
        return None, None

    image_array = np.asarray(bytearray(response.content), dtype=np.uint8)
    img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    
    cv2.imshow(f"{artwork_name}", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return img, artwork_name


if __name__ == "__main__":
    main()
