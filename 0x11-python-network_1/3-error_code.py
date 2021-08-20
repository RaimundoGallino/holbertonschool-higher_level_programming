#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request
to the URL and displays the body of the response (decoded in utf-8).
"""


import urllib.request
from sys import argv


if __name__ == "__main__":

    with urllib.error.URLError.urlopen(argv[1]) as e:
        print (e)
