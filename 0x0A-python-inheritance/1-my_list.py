#!/usr/bin/python3
"""A myList class that inherits from list"""


class MyList(list):
    """My list class"""

    def print_sorted(self):
        """A method that prints list in sorted order"""
        print(sorted(self))
