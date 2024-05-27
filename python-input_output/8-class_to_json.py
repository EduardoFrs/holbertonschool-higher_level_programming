#!/usr/bin/python3
"""8. Class to JSON"""


def class_to_json(obj):
    """function that return the dictionnary description
    with simple data structure for
    JSON serialization of an object"""
    return obj.__dict__
