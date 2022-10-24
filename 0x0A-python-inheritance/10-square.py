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
            string = str(name)
            message = name + " must be an integer"
            raise TypeError(message)
        elif (value <= 0):
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """A rectangle class"""

    def __init__(self, width, height):
        """initiate props"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ a method to get the area of the instance"""
        return (self.__width * self.__height)

    def __str__(self):
        """print in a styled format"""
        part1 = "[Rectangle] "
        part2 = str(self.__width) + "/" + str(self.__height)
        message = part1 + part2
        return (message)


class Square(Rectangle):
    """A class that inherits from rect"""

    def __init__(self, size):
        """iniitiate props"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
