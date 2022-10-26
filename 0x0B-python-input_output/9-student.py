#!/usr/bin/python3
""" a class Student that defines a student"""


class Student:
    """ a student Class"""
    def __init__(self, first_name, last_name, age):
        """initialize instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """that retrieves a dictionary rep of an instance"""
        return (self.__dict__)
