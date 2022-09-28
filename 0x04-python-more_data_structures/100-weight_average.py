#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        score_sum = 0
        weight_sum = 0
        length = len(my_list)
        score_mul_list = list(map(lambda x: x[0] * x[1], my_list))
        weight_list = list(map(lambda x: x[1], my_list))
        for elem in score_mul_list:
            score_sum += elem
        for elem in weight_list:
            weight_sum += elem
        return score_sum / weight_sum
    else:
        return 0
