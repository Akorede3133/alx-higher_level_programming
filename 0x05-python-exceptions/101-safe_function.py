#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    res = None
    try:
        res = fct(*args)
    except (ZeroDivisionError, IndexError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
    return res
