#!/usr/bin/python3
"""a list of lists of integers representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    parent_list = []
    child_list = []
    if n <= 0:
        return []
    else:
        for i in range(1, n + 1):
            j = 1
            child_list = []
            while j <= i:
                num = 1
                child_list.append(num)
            parent_list.append(child_list)
    return parent_list


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))


