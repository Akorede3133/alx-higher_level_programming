#!/usr/bin/python3
def search_replace(my_list, search, replace):
    length = len(my_list)
    for i in range(0, length):
        if my_list[i] == search:
            my_list[i] = replace
    return my_list
