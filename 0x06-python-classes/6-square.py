#!/usr/bin/python3
"""Creating a square class"""


class Square:
    """giving atrributes to the class"""
    def __init__(self, size=0, position=(0, 0)):
        """instantiator for each instances"""
        if position[0] < 0 or position[1] < 0:
            raise TypeError('positon must be a tuple of 2 positive integers')
        else:
            self.__position = position
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """An area method for each instance"""
        return self.__size ** 2

    @property
    def size(self):
        """a getter method to retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """a setter method to set value to value given"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def my_print(self):
        """print a square given the size"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
