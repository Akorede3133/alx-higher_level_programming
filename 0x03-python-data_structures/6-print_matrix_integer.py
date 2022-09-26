#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    height = len(matrix)
    if height == 1:
        print(end="")
    for h in range(0, height):
        width = len(matrix[h])
        for w in range(0, width):
            if w < width - 1:
                print("{:d}".format(int(matrix[h][w])), end=" ")
            else:
                print("{:d}".format(int(matrix[h][w])), end="")
        print()
