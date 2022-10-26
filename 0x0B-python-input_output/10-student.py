#!/usr/bin/python3
""" a class Student that defines a student"""


class Student:
    """ a student Class"""
    def __init__(self, first_name, last_name, age):
        """initialize instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """that retrieves a dictionary rep of an instance"""
        instance_dict = self.__dict__
        new_dict = {}
        if not attrs:
            return (self.__dict__)
        else:
            for key, value in instance_dict.items():
                if key in attrs:
                    new_dict[key] = value
            return (new_dict)
