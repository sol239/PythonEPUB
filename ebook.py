from dataclasses import dataclass, asdict
import zipfile
import os
import os
import re
import xml.etree.ElementTree as ET

epub_path = "C:/Users/david_dyn8g78/Downloads/[Hyperion Cantos 3 ] Simmons, Dan - Endymion (1920, Random House Publishing Group) - libgen.li.epub"
temp_path = os.getcwd() + "/temp"
metadataTags = [
    "title",
    "language",
    "identifier",
    "creator",
    "publisher",
    "date",
    "rights",
]


def find_opf_file(xml_file_path):
    # Read the content of the XML file
    with open(xml_file_path, 'r', encoding='utf-8') as file:
        xml_content = file.read()

    # Regex to find the .opf file path
    opf_pattern = r'full-path="([^"]+\.opf)"'

    # Search for the pattern
    match = re.search(opf_pattern, xml_content)

    # If found, return the .opf file path
    if match:
        return match.group(1)
    else:
        return None

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
        self.ebook = EbookObject(
            title="",
            author="",
            language="",
            publisher="",
            description="",
            format="",
            filename="",
            book_position="",
            book_open_time="",
            book_close_time="",
            book_read_time="",
            book_status="",
            StatRecord1={},
            StatRecord2={},
            navigation_data={},
            ebook_folder_path="",
            ebook_data_folder_path="",
            container_file_path="",
            content_file_path="",
            cover_image_path="",
            json_data_file_path="",
            navis_file_path=""
        )

    def get_epub_content_file_path(self, debug=False):

        try:
            # Construct the path to the container XML file
            xml_file_path = os.path.join(self.ebook.ebook_folder_path, "META-INF", "container.xml")
            self.ebook.container_file_path = xml_file_path
            self.ebook.content_file_path = os.path.join(self.ebook.ebook_folder_path, find_opf_file(xml_file_path))

        except (OSError, IOError) as e:
            # Handle file-related errors
            if debug and "already exists" in str(e):
                print(f"get_epub_content_file_path() - Fail - {e}")
            raise
        except ET.ParseError as e:
            # Handle XML parsing errors
            if debug:
                print(f"get_epub_content_file_path() - XML Parsing Error - {e}")
            raise
        except ValueError as e:
            # Handle cases where the expected XML structure is not found
            if debug:
                print(f"get_epub_content_file_path() - Value Error - {e}")
            raise

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

    def print_ebook_object(self):
        print(asdict(self.ebook))

    def print_xml_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                print(content)  # Print the contents of the XML file
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def add_meta_data(self, content_filepath):

        tree = ET.parse(content_filepath)
        root = tree.getroot()
        #print(root.tag)
        #print(f"root tag = {root[0].tag}")



        for child in root[0]:

            if "title" in child.tag:
                self.ebook.title = child.text
                continue
            elif "creator" in child.tag:
                self.ebook.author = child.text
                continue
            elif "language" in child.tag:
                self.ebook.language = child.text
                continue
            elif "publisher" in child.tag:
                self.ebook.publisher = child.text
                continue
            elif "description" in child.tag:
                self.ebook.description = child.text
                continue
            elif "rights" in child.tag:
                self.ebook.book_status = child.text
                continue
            elif "date" in child.tag:
                self.ebook.date_added = child.text
                continue
            elif "identifier" in child.tag:
                self.ebook.identifier = child.text
                continue

            elif "meta" in child.tag:
                for subchild in child.iter():
                    print(subchild.tag, subchild)



    def load_ebook(self):
        self.extract_epub(self.ebook_filepath, temp_path)
        self.get_epub_content_file_path()
        self.add_meta_data(self.ebook.content_file_path)

        # code cannot set correct cover path




ebook = Ebook(epub_path)
ebook.load_ebook()
ebook.print_ebook_object()


