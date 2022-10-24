#!/usr/bin/python3
"""compare class"""


def inherits_from(obj, a_class):
    """makes comparison"""

    return (issubclass(type(obj), a_class) and a_class != type(obj))
