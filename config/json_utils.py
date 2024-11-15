import json
import os
from quiz_models import Question

# Define the default path to data.json in the config folder
DEFAULT_JSON_PATH = os.path.join('config', 'data.json')

def read_json(file_path=DEFAULT_JSON_PATH):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def write_json(file_path=DEFAULT_JSON_PATH, data=None):
    with open(file_path, 'w') as file:
        json.dump([question.model_dump() for question in data], file, indent=4)

