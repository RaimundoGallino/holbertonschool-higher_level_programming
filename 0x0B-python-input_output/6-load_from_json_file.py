#!/usr/bin/python3
"""
function that reads a text file (UTF8) and prints it to stdout
"""


import json


def load_from_json_file(filename):
    with open(filename, "r", encoding="utf-8") as json_file:
        return json.load(json_file)
