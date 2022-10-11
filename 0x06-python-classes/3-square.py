#!/usr/bin/python3
"""Creating a square class"""


class Square:
    """giving atrributes to the class"""
    def __init__(self, size=0):
        """instantiator for each instances"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
    def area(self):
        """An area method for each instance"""
        return self.__size ** 2
