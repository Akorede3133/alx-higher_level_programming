#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda x: [x[i] ** 2  for i in range(0, len(x))], matrix)))
