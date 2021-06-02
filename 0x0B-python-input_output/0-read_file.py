#!/usr/bin/python3
"""
function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """defining readfile function"""
    with open(filename, encoding="UTF8") as f:
        lines = f.read()
