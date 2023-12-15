"""
Text
"""
import json

def open_text():
    """
    Open text
    """
    with open('text.json', 'r', encoding="utf-8") as file:
        texts = json.load(file)
        return texts
