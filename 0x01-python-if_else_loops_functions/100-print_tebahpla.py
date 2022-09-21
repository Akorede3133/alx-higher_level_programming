#!/usr/bin/python3
i = 122
while i >= 97:
    if i % 2 != 0:
        diff = 32
    else:
        diff = 0
    print("{}".format(chr(i - diff)), end="")
    i = i - 1
