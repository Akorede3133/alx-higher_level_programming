#!/usr/bin/python3
"""a func that returns a JSON rep of an obj"""
import json


def to_json_string(my_obj):
    """returns json rep"""
    data = json.dumps(my_obj, sort_keys=True)
    return (data)
