#!/usr/bin/python3

for num in range(10):
    for sec in range(10):
        if (sec > num):
            if sec != 9 or num != 8:
                print("{}{}".format(num, sec), end=", ")
            else:
                print("{}{}".format(num, sec))
