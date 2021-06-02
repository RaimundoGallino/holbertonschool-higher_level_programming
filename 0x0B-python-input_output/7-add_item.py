#!/usr/bin/python3
"""
function that reads a text file (UTF8) and prints it to stdout
"""


import json
from sys import argv
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


obj = []

if (path.exists('add_item.json')):
    obj = load_from_json_file('add_item.json')

for i in range(1, len(argv)):
    obj.append(argv[i])
save_to_json_file(obj, 'add_item.json')
