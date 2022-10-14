#!/usr/bin/python3
"""A class that defines a sqaure"""


class Square:
    """A square class"""
    def __init__(self, size=0):
        """initiate prop to instances"""
        self.size = size

    @property
    def size(self):
        """method to get size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be a number')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """method to return area"""
        return (self.__size ** 2)

    def __bool__(self):
        """returning the boolean value of instance attribute"""
        return bool(self.__size)

    def __eq__(self, other):
        """checking for equality of square areas"""
        return bool(Square(self.area() == other.area()))

    def __ne__(self, other):
        """checking for inequality of square areas"""
        return bool(Square(self.area() != other.area()))

    def __gt__(self, other):
        """checking for equality of square areas"""
        return bool(Square(self.area() > other.area()))

    def __lt__(self, other):
        """checking for equality of square areas"""
        return bool(Square(self.area() < other.area()))

    def __ge__(self, other):
        """checking for equality of square areas"""
        return bool(Square(self.area() >= other.area()))

    def __le__(self, other):
        """checking for equality of square areas"""
        return bool(Square(self.area() <= other.area()))
