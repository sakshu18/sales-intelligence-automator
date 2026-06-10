import json
from datetime import datetime

def save_json(data, filepath):

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )


def read_json(filepath):

    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)
    
def generate_timestamp():

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")