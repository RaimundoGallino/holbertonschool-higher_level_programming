#!/usr/bin/python3
"""
class inherited from list
"""


class MyList(list):
    """define class MyList"""

    def print_sorted(self):
        """ prints the list, but sorted (ascending sort)"""
        print(sorted(self))
