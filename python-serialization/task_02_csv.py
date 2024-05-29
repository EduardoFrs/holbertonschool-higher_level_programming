#!/usr/bin/python3
"""2. Converting CSV Data to JSON Format"""


import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, 'r', encoding="utf-8") as csvf:
            csvReader = csv.DictReader(csvf)
            data = [row for row in csvReader]

        with open('data.json', 'w', encoding="utf-8") as jsonf:
            jsonf.dump(data, jsonf, indent=4)

        return True

    except FileNotFoundError:
        print(f"Error: The file {csv_filename} was not found")
        return False

    except Exception as e:
        print(f"An error occured: {e}")
        return False
