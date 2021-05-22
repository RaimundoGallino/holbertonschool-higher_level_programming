#!/usr/bin/python3
"""
adds two integers
"""


def add_integer(a, b=98):
    """Adds integers function"""
    if isinstance(a, float): a = int(a)
    if isinstance(b, float): b = int(b)
    if isinstance(a, int) is False:
        raise TypeError("a must be an integer")
    elif isinstance(b, int) is False:
        raise TypeError("b must be an integer")
    else:
        return a + b
