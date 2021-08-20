#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request
to the URL and displays the body of the response (decoded in utf-8).
"""


import requests
from sys import argv


if __name__ == "__main__":

    token = argv[2]
    owner = argv[1]
    query_url = "https://api.github.com/user"

    r = requests.get(query_url, auth=(owner, token))
    print(r.json().get('id'))
