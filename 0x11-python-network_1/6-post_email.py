#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request
to the URL and displays the body of the response (decoded in utf-8).
"""


import requests
from sys import argv


if __name__ == "__main__":
    r = requests.post(argv[1], data={'email':argv[2]})
    print(r)
