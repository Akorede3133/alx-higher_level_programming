#!/usr/bin/python3
""" returns a list of lists of integers reping pascal"""


def pascal_triangle(n):
    """ returns a list of lists of integers reping pascal"""
    if n <= 0:
        return ([])
    if n == 1:
        parent = [[1]]
    else:
        parent = [[1], [1, 1]]
    for i in range(0, n - 2):
        child = []
        temp = parent[-1]
        for j in range(0, len(temp) - 1):
            if j == 0:
                value = 1
            else:
                value = temp[j] + temp[j - 1]
            child.append(value)
        child.append(1)
        parent.append(child)
    return (parent)
