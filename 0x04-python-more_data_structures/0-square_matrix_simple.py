#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    #new_matrix = list(map(lambda x: [x[0] **2, x[1] ** 2, x[2] ** 2], matrix))
    final_matrix = []
    length = len(matrix)
    for h in range(0, length):
        new_matrix = []
        for w in range(0, len(matrix[h])):
            new_matrix.append(matrix[h][w] ** 2)
        final_matrix.append(new_matrix)
    return final_matrix
