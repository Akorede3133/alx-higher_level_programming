#!/usr/bin/python3
"""a function that writes an Object to a text file, using a JSON rep"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON rep"""
    with open(filename, 'w') as my_file:
        data = json.dumps(my_obj)
        my_file.write(data)
