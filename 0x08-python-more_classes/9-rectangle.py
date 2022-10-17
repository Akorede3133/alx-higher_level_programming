#!/usr/bin/python3
"""Defining a rectangle class"""


class Rectangle:
    number_of_instances = 0
    print_symbol = "#"
    """listing out its attributes"""
    def __init__(self, width=0, height=0):
        """initiator of each instance"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def __str__(self):
        """return a string format of the instance"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    print(str(self.print_symbol), end="")
                print()
            return ("")
    def __repr__(self):
        """return a string representation of the instance"""
        width = self.__width
        height = self.__height
        return "Rectangle(" + str(width) + ", " + str(height) + ")"

    def __del__(self):
        """deletes the instance"""
        type(self).number_of_instances -= 1
        del self
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns bigger"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        else:
            if rect_1.area() > rect_2.area():
                return (rect_1) 
            elif rect_2.area() > rect_1.area():
                return (rect_2)
            else:
                return (rect_1)

    @classmethod
    def square(cls, size=0):
        """returns a square instance"""
        return cls(size, size)
