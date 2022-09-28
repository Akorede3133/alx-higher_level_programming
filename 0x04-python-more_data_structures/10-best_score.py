#!/usr/bin/python3
def best_score(a_dictionary):
    highest = 0
    if not a_dictionary:
        return
    for key, value in a_dictionary.items():
        if a_dictionary[key] > highest:
            highest = a_dictionary[key]
        else:
            highest = highest
    for key, value in a_dictionary.items():
        if value == highest:
            return key
