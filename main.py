from epub_handler import Ebook
from epub_serializer import serialize, deserialize, load_json

if __name__ == '__main__':
    ebook = Ebook("C:/Users/david_dyn8g78/Downloads/Endymion - Dan Simmons.epub")

    # print  ebook's attributes
    print(vars(ebook))

    # print ebook's title
    print(ebook.title)

    # save ebook into .json file
    serialize(ebook, save=True, save_dest="")

    # load ebook from .json file
    ebook = deserialize("data.json")
