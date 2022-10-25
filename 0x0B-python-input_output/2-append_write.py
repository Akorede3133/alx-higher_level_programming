#!/usr/bin/python3
"""A fun that appends to a file"""


def append_write(filename="", text=""):
    """appends to a file"""
    with open(filename, 'a', encoding="utf-8") as my_file:
        num = my_file.write(text)
        return (num)
