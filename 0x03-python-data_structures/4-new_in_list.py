#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_len = len(my_list) - 1
    if idx < 0 or idx > list_len:
        return my_list[:]
    else:
        copied_list = my_list[:]
        copied_list[idx] = element
        return copied_list
