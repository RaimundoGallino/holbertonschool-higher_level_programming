#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request
to the URL and displays the body of the response (decoded in utf-8).
"""


import requests
from sys import argv

bad_r = requests.get(argv[1])

bad_r.raise_for_status()
print('Error Code: ' + str(bad_r.status_code))