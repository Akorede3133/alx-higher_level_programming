#!/usr/bin/python3
"""a script that adds all args to list, and then save them to a file"""
import sys
if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(): 
    """a script that adds all args to list, and then save them to a file"""
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_items.json")

add_item()
