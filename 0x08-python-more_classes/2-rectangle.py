#!/usr/bin/python3
"""Defining a rectangle class"""


class Rectangle:
    """listing out its attributes"""
    def __init__(self, width=0, height=0):
        """initiator of each instance"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value


    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """returns the area of the instance"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of an instance"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            hp = 2 * (self.__height)
            wp = 2 * (self.__width)
            return (hp + wp)
