#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_new_list = set(my_list)
    res = 0
    for elem in my_new_list:
        res += elem
    return res
