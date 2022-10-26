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
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            for key, value in instance_dict.items():
                if key in attrs:
                    new_dict[key] = value
            return (new_dict)
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
