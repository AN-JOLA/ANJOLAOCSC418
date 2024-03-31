import re
import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

# Art collection in dictionary
art_collections = {
    'traditional': {
        'Gelede Headdress': 'https://museum.pau.edu.ng/images/gelede-headdress-2/IMG_0024_1.JPG',
        'Benin Head': 'https://museum.pau.edu.ng/images/benin-head/AS5A7600-1.jpg',
        'Yoruba Human Face': 'https://museum.pau.edu.ng/images/yoruba-human-face/2019.0120-UNKNOWN-1.jpg',
        'Portuguese Soldier': 'https://museum.pau.edu.ng/images/portuguese-soldier/2019.0124-UNKNOWN.jpg',
        'Traditional Bell': 'https://museum.pau.edu.ng/images/traditional-bell/2019.0133-UNKNOWN.jpg',
        'Ife Bronze Head': 'https://museum.pau.edu.ng/images/ife-bronze-head/Ife-Royal-head-Bronze-min.jpg'
    },
    'contemporary': {
        'In The Country': 'https://museum.pau.edu.ng/images/in-the-country/2019.0784.png',
        'Durbar': 'https://museum.pau.edu.ng/images/durbar-1/2019.0712.jpg',
        'Fulani Dancers Part I': 'https://museum.pau.edu.ng/images/fulani-dancers-part-i/2019.0390.jpg',
        'Eti Osa': 'https://museum.pau.edu.ng/images/eti-osa/2019.0384.jpg',
        'The Landscape No Image': 'https://museum.pau.edu.ng/images/the-landscape-1/2019.0383.jpg',
        'Flexibility': 'https://museum.pau.edu.ng/images/flexbility/2019.0710.jpg'
    },
    'modern': {
        'Nnamdi Azikiwe': 'https://museum.pau.edu.ng/images/nnamdi-azikiwe/2019.0150.Lasekan.jpg',
        'Iya Abikun': 'https://museum.pau.edu.ng/images/iya-abikun/2019.0130.-Omopae.jpg',
        'Red Sky': 'https://museum.pau.edu.ng/images/red-sky/2019.0108.-Dale.jpg',
        'Landscape from the North': 'https://museum.pau.edu.ng/images/land-scape-from-the-north/2019.0117.-Oshinowo.jpg'
    }
}

def access_images():
    # Validating email
    email = input("Enter your email address ending with @pau.edu.ng: ")
    if not validate_email(email):
        print("Invalid email format. Please enter a valid email.")
        return

    # Validating age
    age = input("Enter your age: ")
    if not check_age(age):
        print("Invalid age. Please enter an age above 18.")
        return
    age = int(age)

    # Displaying categories
    categories = list(art_collections.keys())
    print("\nSelect a category by entering a number:")

    #enumerate lists things out, 0 is usually default, 1 means it'll start from 1
    for index, category in enumerate(categories, 1):
        print(f"{index}. {category}")
    
    # Validating category
    category_number = input("Enter the number corresponding to the desired category: ")
    if not category_number.isdigit() or not (1 <= int(category_number) <= len(categories)):
        print("Invalid category number. Please enter a valid category number.")
        return
    category_number = int(category_number)

    category = categories[category_number - 1]
    artworks = art_collections[category]

    # Displaying artworks
    print(f"\nArtworks in the {category} category:")
    for index, (artwork_name, _) in enumerate(artworks.items(), 1):
        print(f"{index}. {artwork_name}")

    # Getting user choice
    artwork_number = input("\nEnter the number corresponding to the desired artwork to view its image: ")
    if not artwork_number.isdigit() or not (1 <= int(artwork_number) <= len(artworks)):
        print("Invalid artwork number. Please enter a valid artwork number.")
        return
    artwork_number = int(artwork_number)

    # Displaying image
    _, artwork_url = list(artworks.items())[artwork_number - 1]
    response = requests.get(artwork_url)
    img = Image.open(BytesIO(response.content))
    
    plt.imshow(img)
    plt.axis('off')  # Turn off axis numbers and ticks
    plt.title(list(artworks.keys())[artwork_number - 1])
    plt.show()

def validate_email(email):
    # Regular expression pattern for email validation
    pattern = r"^[a-zA-Z0-9._%+-]+@pau\.edu\.ng$"
    return re.match(pattern, email) is not None

def check_age(age):
    return age.isdigit() and int(age) > 18


# Main program

print("Welcome to the Yemisi Shyllon Museum of Art!")
access_images()
