#!/usr/bin/python3
"""5. Save Object to a file"""


import json


def save_to_json_file(my_obj, filename):
    """function that write an object to a txt file,
    using JSON representation"""
    with open(filename, 'w', encoding="utf-8") as f:
        return json.dump(my_obj, f)
