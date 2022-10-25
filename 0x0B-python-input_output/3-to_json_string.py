#!/usr/bin/python3
import json
"""a func that returns a JSON rep of an obj"""


def to_json_string(my_obj):
    """returns json rep"""
    data = json.dumps(my_obj, sort_keys=True)
    return (data)
