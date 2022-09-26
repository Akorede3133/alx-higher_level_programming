#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_len = len(my_list)
    for elemIndex in range(list_len, 0, -1):
        print("{:d}".format(int(my_list[elemIndex - 1])))
my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
