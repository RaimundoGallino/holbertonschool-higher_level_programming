#!/usr/bin/python3
"""
function that reads a text file (UTF8) and prints it to stdout
"""

import json


def class_to_json(obj):
    return (obj.__dict__)
