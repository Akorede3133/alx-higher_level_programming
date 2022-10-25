#!/usr/bin/python3
"""A func that writes to a file"""


def write_file(filename="", text=""):
    """write text to file"""
    with open(filename, mode='w', encoding="utf-8") as my_file:
        num_of_char = my_file.write(text)
        return (num_of_char)
