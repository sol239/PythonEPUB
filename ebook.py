from dataclasses import dataclass, asdict

@dataclass
class Ebook:
    title: str
    author: str
    language: str
    publisher: str
    description: str
    # date_added: str
    # date_last_opened: str
    format: str
    filename: str
    # book_position: str
    # book_open_time: str
    # book_close_time: str

