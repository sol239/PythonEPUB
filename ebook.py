from dataclasses import dataclass

@dataclass
class EbookObject:

    """
    A class representing an ebook

    Attributes
        title (str): The title of the ebook
        author (str): The author of the ebook
        ...
    """

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
    nav_file_path: str
    date_added: str
    date_last_opened: str
