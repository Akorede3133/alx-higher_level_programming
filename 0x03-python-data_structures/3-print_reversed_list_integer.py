#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_len = len(my_list)
    for elemIndex in range(list_len, 0, -1):
        print(elemIndex)
        print("{:d}".format(my_list[elemIndex - 1]))
