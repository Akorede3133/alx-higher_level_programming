#!/usr/bin/python3
"""a func that returns a JSON rep of an obj"""
import json


def from_json_string(my_obj):
    """returns json rep"""
    data = json.loads(my_obj)
    return (data)
