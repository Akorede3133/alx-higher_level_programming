#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    length = len(my_list)
    new_list = []
    if idx < 0 or idx > length - 1:
        return my_list[:]
    else:
        for elem in my_list:
            if my_list.index(elem) == idx:
                my_list.remove(elem)
        return (my_list)
