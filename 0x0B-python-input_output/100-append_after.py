#!/usr/bin/python3
""" a function that inserts a line of text to a file,"""


def append_after(filename="", search_string="", new_string=""):
    """ a function that inserts a line of text to a file,"""
    string = ""
    with open(filename, encoding='utf-8') as my_file:
        for line in my_file:
            if search_string in line:
                line += new_string
            else:
                line = line
            string += line
    with open(filename, 'w', encoding='utf-8') as my_file:
        my_file.write(string)
