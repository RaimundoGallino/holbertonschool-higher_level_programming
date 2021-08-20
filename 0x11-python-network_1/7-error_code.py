#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request
to the URL and displays the body of the response (decoded in utf-8).
"""


import requests
from sys import argv

bad_r = requests.get(argv[1])
if str(bad_r.status_code) != '200':
    print('Error Code: ' + str(bad_r.status_code))
else:
    print(bad_r.text)