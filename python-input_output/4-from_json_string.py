#!/usr/bin/python3
"""4. From JSON string to Object"""


import json


def from_json_string(my_str):
    """function tthat return an object represented by a JSON string"""
    return json.loads(my_str)
