#!/usr/bin/python3
"""
function that reads a text file (UTF8) and prints it to stdout
"""


import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w+", encoding="utf-8") as json_file:
        return json.dump(my_obj, json_file)
