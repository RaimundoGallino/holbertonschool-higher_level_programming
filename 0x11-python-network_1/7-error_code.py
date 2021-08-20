#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request
to the URL and displays the body of the response (decoded in utf-8).
"""


import requests
from sys import argv


if __name__ == "__main__":
    bad_r = requests.get(argv[1])
    if bad_r.status_code >= 400:
        print('Error Code: {:d}'.format(bad_r.status_code))
    else:
        print(bad_r.text)
