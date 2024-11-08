import json
from dataclasses import asdict

from ebook import EbookObject

def serialize(ebook:EbookObject, save:bool, save_dest:str = "") -> str:
    json_file = json.dumps(asdict(ebook))
    if (save):
        save_json(json_file, save_dest)
    return json_file

def deserialize(json_file_path:str) -> EbookObject:
    file = open(json_file_path, "r", encoding="utf-8")
    ebook_data = json.load(file)
    ebook = EbookObject(**ebook_data)
    return ebook

def save_json(json:str,json_file_path:str):
    if json_file_path == "":
        json_file_path = "data.json"
    file = open(json_file_path, "w", encoding="utf-8")
    file.write(json)
    file.close()
    return

def load_json(json_file_path:str) -> str:
    file = open(json_file_path, "r", encoding="utf-8").read()
    return file