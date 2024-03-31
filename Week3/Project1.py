#he Yemisi Shyllon Museum of Art is a university museum with the purpose of serving and engaging diverse audiences by advancing knowledge about Nigerian art 
# and by offering exhibitions and educational programs that enable them to learn about art and through art. 
# The museum has 3 main art collection categories: traditional art, modern art, and contemporary art. 
# Dr Jess Castellote, the Director has recently contacted you as a computer vision developer to build an application that would enable the visitors to 
# access images from each category, using the image transformation methods studied on the collection, following the criteria:
#The visitor must have a valid email, must be above 18 years and the choice of collection category of interest must be specified.

art_collections = {
    'traditional': {
        'Gelede Headdress': 'https://museum.pau.edu.ng/images/gelede-headdress-2/IMG_0024_1.JPG',  
        'Benin Head': 'https://museum.pau.edu.ng/images/benin-head/AS5A7600-1.jpg',  
        'Yoruba Human Face': 'https://museum.pau.edu.ng/images/yoruba-human-face/2019.0120-UNKNOWN-1.jpg',   
        'Portugese Soldier': 'https://museum.pau.edu.ng/images/portuguese-soldier/2019.0124-UNKNOWN.jpg',   
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
        'Land scape from the North': 'https://museum.pau.edu.ng/images/land-scape-from-the-north/2019.0117.-Oshinowo.jpg',   
    }
}


def access_images(email, age, category):
    if validate_email(email) and check_age(age) and category in ['traditional', 'modern', 'contemporary']:
        
        pass
    else:
        print("Invalid input. Please provide a valid email, age above 18, and a valid category.")

def validate_email(email):
    
    pass

def check_age(age):
    
    pass

access_images(email, age, category)