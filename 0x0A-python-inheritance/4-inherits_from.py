#!/usr/bin/python3
"""
returns True if the object is an instance
of a class that inherited (directly or indirectly)
from the specified class; otherwise False.
"""


def inherits_from(obj, a_class):
    if (isinstance(obj, a_class) != 0):
        return True
    else:
        return False
