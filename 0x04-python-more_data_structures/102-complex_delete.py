#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_to_delete = []
    if value in a_dictionary.values():
        for key, v in a_dictionary.items():
            if value == v:
                key_to_delete.append(key)
        for elem in key_to_delete:
            del a_dictionary[elem]
    return a_dictionary
