#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request
to the URL and displays the body of the response (decoded in utf-8).
"""


import requests
from sys import argv

r = requests.get(argv[1])
print(r.headers['X-Request-Id'])
