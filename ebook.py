import os
import re
import shutil
import xml.etree.ElementTree as ET
import zipfile
from dataclasses import dataclass, asdict
from datetime import datetime

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
    nav_file_path: str
    date_added: str
    date_last_opened: str

class Ebook(EbookObject):
    def __init__(self, ebook_filepath: str):
        super().__init__(
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
            nav_file_path="",
            date_added="",
            date_last_opened=""
        )

        self.ebook_filepath = ebook_filepath

        self.load_ebook()

    def get_epub_content_file_path(self, debug=False):

        try:
            # Construct the path to the container XML file
            xml_file_path = os.path.join(self.ebook_folder_path, "META-INF", "container.xml")
            self.container_file_path = xml_file_path
            self.content_file_path = os.path.join(self.ebook_folder_path, find_opf_file(xml_file_path))

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

        self.ebook_folder_path = destination_path
        self.ebook_data_folder_path = destination_path + "DATA"
        self.format = "epub"
        self.filename = os.path.basename(epub_filepath)

        # --------- TBD -------------
        self.nav_file_path = ""
        self.date_added = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.date_last_opened = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # ----------------------------

    def print_ebook_object(self):
        ebook_dict = asdict(self)

        list_correct = []
        list_incorrect = []

        for key, value in ebook_dict.items():
            #print(f"{key}: {value}")
            if value == {}:
                list_incorrect.append(key)
            elif value != "":
                list_correct.append(f"{key}: {value}")
            else:
                list_incorrect.append(key)

        print("Found:")
        for item in list_correct:
            print(f" - {item}")
        print("\nNot Found:")
        for item in list_incorrect:
            print(f" - {item}")

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
        xml_file = open(content_filepath, 'r', encoding='utf-8')

        #print(root.tag)
        #print(f"root tag = {root[0].tag}")

        for child in root[0]:

            if "title" in child.tag:
                self.title = child.text
                continue
            elif "creator" in child.tag:
                self.author = child.text
                continue
            elif "language" in child.tag:
                self.language = child.text
                continue
            elif "publisher" in child.tag:
                self.publisher = child.text
                continue
            elif "description" in child.tag:
                self.description = child.text
                continue
            elif "rights" in child.tag:
                self.book_status = child.text
                continue
            elif "date" in child.tag:
                self.date_added = child.text
                continue
            elif "identifier" in child.tag:
                self.identifier = child.text
                continue

            # cover path setter
            elif "meta" in child.tag:
                for subchild in child.iter():
                    if "name" in subchild.attrib:
                        if subchild.attrib["name"] == "cover":
                            id = subchild.attrib["content"]

                            for line_number, line in enumerate(xml_file, start=1):
                                if id in line:
                                    if ("href" in line):
                                        cover_path = (line.split()[1].split("href=")[1].replace("\"", ""))
                                        self.cover_image_path = os.path.normpath(os.path.join(os.path.dirname(self.content_file_path), cover_path))

        xml_file.close()

    def add_navigation_data(self, content_filepath):
        tree = ET.parse(content_filepath)
        root = tree.getroot()
        xml_file = open(content_filepath, 'r', encoding='utf-8')
        nav_data = {}

        chapters = []

        for i in range(len(root)):
            if "manifest" in root[i].tag:
                print("Manifest found")
                root = root[i]
                x = 0
                for child in root:
                    if "item" in child.tag:
                        id = child.attrib["id"]
                        href = child.attrib["href"]
                        nav_data[id] = href
                        chapter_html = os.path.join(self.ebook_folder_path, href)
                        nav_data[x] = chapter_html
                        x += 1
        self.navigation_data = nav_data
    def delete_archive(self):
        # remove temp directory
        shutil.rmtree(self.ebook_folder_path)

    def load_ebook(self):
        self.extract_epub(self.ebook_filepath, temp_path)
        self.get_epub_content_file_path()
        self.add_meta_data(self.content_file_path)
        self.add_navigation_data(self.content_file_path)
