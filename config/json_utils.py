import json
import streamlit as st
import os

# Define the default path to data.json in the config folder
DEFAULT_JSON_PATH = os.path.join('config', 'data.json')

def read_json(file_path=DEFAULT_JSON_PATH):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def write_json(file_path=DEFAULT_JSON_PATH, data=None):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
