#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    length = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
        print()
        return i + 1
    except (IndexError, UnboundLocalError):
        print()
        for elem in my_list:
            length += 1
        return length
