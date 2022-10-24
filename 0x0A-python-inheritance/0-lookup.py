#!/usr/bin/python3
"""returns list"""


def lookup(obj):
    """look up"""
    attr_and_methods = dir(obj)
    return (attr_and_methods)
