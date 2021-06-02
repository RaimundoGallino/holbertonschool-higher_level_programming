#!/usr/bin/python3
"""
MyInt that inherits from int
"""

def add_attribute(objclass, attr, newattr):
    """MyInt that inherits from int"""
    if not hasattr(objclass, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(objclass, attr, newattr)
