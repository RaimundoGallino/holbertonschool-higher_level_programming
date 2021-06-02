#!/usr/bin/python3
"""
function that reads a text file (UTF8) and prints it to stdout
"""


import json


def from_json_string(my_str):
    """defining to_json_string function"""
    return json.loads(my_str)
