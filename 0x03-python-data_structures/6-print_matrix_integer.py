#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    height = len(matrix)
    if height == 1:
        print(end="")
    for h in range(0, height):
        for w in range(0, len(matrix[h])):
            if w < len(matrix[h]) - 1:
                print("{:d}".format(int(matrix[h][w])), end=" ")
            else:
                print("{:d}".format(int(matrix[h][w])), end="")
        print()
