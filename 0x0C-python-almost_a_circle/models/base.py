#!/usr/bin/python3
"""A base class"""


class Base:
    """A base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initiate instances"""
        if self.id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
