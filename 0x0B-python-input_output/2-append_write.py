#!/usr/bin/python3
"""
function that reads a text file (UTF8) and prints it to stdout
"""


def append_write(filename="", text=""):
    """defining readfile function"""
    with open(filename, "a", encoding="utf-8") as f:
        fulltext = f.write(text)
    return(fulltext)
