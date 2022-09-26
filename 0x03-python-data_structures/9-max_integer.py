#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    else:
        max_num = my_list[0]
        for elem in my_list:
            if max_num > elem:
                max_num = max_num
            else:
                max_num = elem
    return (max_num)
