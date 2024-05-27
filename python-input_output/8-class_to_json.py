#!/usr/bin/python3
"""8. Class to JSON"""


import json


def class_to_json(obj):
    """function that return the dictionnary description
    with simple data structure for
    JSON serialization of an object"""
    json_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value
    return json_dict
