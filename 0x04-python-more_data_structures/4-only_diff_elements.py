#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = []
    list_from_set = list(set_1)
    list_from_set.extend(list(set_2))
    for elem in list_from_set:
        if elem not in set_1 or elem not in set_2:
            new_set.append(elem)
    return set(new_set)
    # return set_2 ^  set_2
