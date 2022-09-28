#!/usr/bin/python3
from functools import reduce
def weight_average(my_list=[]):
    if my_list:
        length = len(my_list)
        mulVal = list(map(lambda x: x[0] * x[1], my_list))
        summation = list([reduce(lambda x, y: x + y, mulVal)])
        weightVal = list(map(lambda x: x[1], my_list))
        weightSum = list([reduce(lambda x, y: x + y, weightVal)])
        return summation[0]/weightSum[0]
