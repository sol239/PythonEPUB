from dataclasses import dataclass, asdict
import zipfile
import os

epub_path = "C:/Users/david_dyn8g78/Downloads/[Hyperion Cantos 3 ] Simmons, Dan - Endymion (1920, Random House Publishing Group) - libgen.li.epub"
temp_path = os.getcwd() + "/temp"

@dataclass
class EbookObject:
    title: str
    author: str
    language: str
    publisher: str
    description: str
    # date_added: str
    # date_last_opened: str
    format: str
    filename: str
    book_position: str
    book_open_time: str
    book_close_time: str
    book_read_time: str
    book_status: str
    StatRecord1: dict
    StatRecord2: dict
    navigation_data: dict
    ebook_folder_path: str
    ebook_data_folder_path: str
    container_file_path: str
    content_file_path: str
    cover_image_path: str
    json_data_file_path: str
    navis_file_path: str

class Ebook:
    def __init__(self, ebook_filepath: str):
        self.ebook_filepath = ebook_filepath
        self.ebook = EbookObject

    def extract_epub(self, epub_filepath: str, destination_path: str):
        with zipfile.ZipFile(epub_filepath, 'r') as zip_ref:
            zip_ref.extractall(destination_path)

        self.ebook.ebook_folder_path = destination_path
        self.ebook.ebook_data_folder_path = destination_path + "DATA"
        self.ebook.format = "epub"
        self.ebook.filename = os.path.basename(epub_filepath)

        # --------- TBD -------------
        self.ebook.navis_file_path = ""
        self.ebook.date_added = ""
        self.ebook.date_last_opened = ""
        # ----------------------------


ebook = Ebook(epub_path)
ebook.extract_epub(epub_path, temp_path)
