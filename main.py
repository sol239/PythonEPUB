from epub_handler import Ebook
from epub_serializer import serialize, deserialize

if __name__ == '__main__':
    ebook = Ebook("demo/epub samples/sample1.epub")

    # print  ebook's attributes
    print(vars(ebook))

    # print ebook's title
    print(ebook.title)

    # save ebook into .json file
    serialize(ebook, save=True, save_dest="")

    # load ebook from .json file
    ebook = deserialize("data.json")
