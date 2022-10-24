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
            raise TypeError(f"{name} must be an integer")
        elif (value <= 0):
            raise ValueError(f"{name} must be greater than 0")
