#!/usr/bin/python3
def read_file(filename=""):
    """a func to read from a file"""
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read())
