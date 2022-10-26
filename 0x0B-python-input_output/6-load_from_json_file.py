#!/usr/bin/python3
"""a function that creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """a function that creates an Object from a JSON file"""
    with open(filename) as my_file:
        data = json.load(my_file)
        return (data)
