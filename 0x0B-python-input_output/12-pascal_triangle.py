#!/usr/bin/python3
""" returns a list of lists of integers reping pascal"""


def pascal_triangle(n):
    """ returns a list of lists of integers reping pascal"""
    if n <= 0:
        return []
    parent = [[1]]
    for i in range(0, n - 1):
        temp = parent[i]
        child = []
        for j in range(0, len(temp)):
            if j == 0:
                value = 1
            else:
                value = temp[j] + temp[j - 1]
            child.append(value)
        child.append(1)
        parent.append(child)
    return (parent)
