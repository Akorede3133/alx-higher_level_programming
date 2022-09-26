#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res = ()
    for i in range(0, 2):
        if len(tuple_a) < 2:
            tuple_a += (0,)
    for i in range(0, 2):
        if len(tuple_b) < 2:
            tuple_b += (0,)
    for i in range(0, 2):
        res += (tuple_a[i] + tuple_b[i],)
    return(res)
tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)
print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
