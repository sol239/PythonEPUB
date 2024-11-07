from epub_handler import Ebook
from epub_serializer import serialize, deserialize, load_json

if __name__ == '__main__':
    ebook = Ebook("C:/Users/david_dyn8g78/Downloads/Endymion - Dan Simmons.epub")

    # print
    print(vars(ebook))

    serialize(ebook, save=True)

    print(vars(deserialize("data.json")))




