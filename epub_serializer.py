import json
import os
from dataclasses import dataclass, asdict
from idlelib.iomenu import encoding

from epub_handler import Ebook
from ebook import EbookObject

def serialize(ebook:EbookObject, save:bool, save_dest:str = ""):
    json_file = json.dumps(asdict(ebook))
    if (save):
        save_json(json_file, save_dest)
    return json_file

def deserialize():

    return

def save_json(json:str,json_file_path:str):
    if json_file_path == "":
        json_file_path = "data.json"
    file = open(json_file_path, "w", encoding="utf-8")
    file.write(json)
    file.close()
    return

def load_json(json_file_path:str):
    return