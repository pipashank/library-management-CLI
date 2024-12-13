
import json

def load_file(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_file(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
