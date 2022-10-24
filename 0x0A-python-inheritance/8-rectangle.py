#!/usr/bin/python3
"""A  BaseGeometry Class"""


class BaseGeometry:
    """defining a base geo class"""

    def area(self):
        """ a method to get the area of the instance"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates values"""
        if (type(value) != int):
            message = f"{name} must be an integer"
            raise TypeError(message)
        elif (value <= 0):
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """A rectangle class"""

    def __init__(self, width, height):
        """initiate props"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
