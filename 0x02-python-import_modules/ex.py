#!/usr/bin/python3

def example():
    y = 1.0
    for _ in range(20):
        print(y)
        y = y * 1.5
        return y

import dis
dis.dis(example)
