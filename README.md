# PythonEPUB

Python library to handle `.epub` ebook file format with option to save ebook’s data as `.json`.

---

### Code structure

- **demo/**
    - **epub samples/**
        - sample1.epub
        - sample2.epub
        
        *samples are used for unittesting and demo*
        
    - **demo.ipynb** = jupyter notebook with demo of the library
- **tests/**
    - **mainTest.py** = unittesting
- **.github/**
    - **workflows/**
        - **main.yml** = used for github actions
- **ebook.py** = .py file with the definition of ebook data class object
- **epub_handler.py** = .py file responsible for obtaining data from .epub
- **epub_serializer.py** = .py file responsible for json (de)serialization
- **main.py**  ****= .py demo file

---

### How to use

- download the zip archive of the repository and then you can use the library this way:
- you can try demo in **`demo.ipynb`**
    
    ```python
    from epub_handler import Ebook
    from epub_serializer import serialize, deserialize
    
    # open .epub file
    ebook = Ebook(".epub file path")
    
    # comment to save extracted epub archive, otherwise it is deleted
    ebook.delete_archive()
    
    # print all ebook's attributes
    print(vars(ebook))
    '''
    {'title': 'Endymion', 
    'author': 'Dan Simmons', 
    'language': 'en-US', 
    'publisher': 'Random House Publishing Group', 'description': '', 'format': 'epub',
    'filename': 'Endymion - Dan Simmons.epub', 'book_position': '', 'book_open_time': '', 
    'book_close_time': '', 'book_read_time': '', 'book_status': 'Copyright © 1995 by Dan Simmons', 
    'StatRecord1': {}, 'StatRecord2': {}, 'navigation_data': {0: 'C:\\Users\\xx\\PycharmProjects\\PythonEPUB/temp\\Simm_9780307781918_epub_ncx_r1.ncx', 1: 'C:\\Users\\xx\\PycharmProjects\\PythonEPUB/temp\\OEBPS/Simm_9780307781918_epub_cvi_r1.htm'}, 
    'ebook_folder_path': 'C:\\Users\\xx\\PycharmProjects\\PythonEPUB/temp', 
    'ebook_data_folder_path': 'C:\\Users\\xx\\PycharmProjects\\PythonEPUB/tempDATA', 
    'container_file_path': 'C:\\Users\\xx\\PycharmProjects\\PythonEPUB/temp\\META-INF\\container.xml', 
    'content_file_path': 'C:\\Users\\xx\\PycharmProjects\\PythonEPUB/temp\\Simm_9780307781918_epub_opf_r1.opf', 
    'cover_image_path': 'C:\\Users\\x\\PycxharmProjects\\PythonEPUB\\temp\\OEBPS\\images\\Simm_9780307781918_epub_cvi_r1.jpg', 
    'json_data_file_path': '', 
    'nav_file_path': '', 
    'date_added': '2011-01-05', 
    'date_last_opened': '2024-11-07 14:21:45', 
    'ebook_filepath': 'C:/Users/xx/Downloads/Endymion - Dan Simmons.epub', 
    'identifier': '978-0-307-78191-8'}
    '''
    
    # Print specified attributes
    print(ebook.title)
    # Endymion
    
    print(ebook.author)
    # Dan Simmons
    
    # save ebook into .json file
    serialize(ebook, save=True, save_dest="")
    
    # load ebook from .json file
    ebook = deserialize("data.json")
    ```
    

---