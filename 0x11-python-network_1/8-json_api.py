#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request
to the URL and displays the body of the response (decoded in utf-8).
"""


import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) != 1:
        q = argv[1]
    else: q = ""

    data = {'q': q}

    r = requests.post('http://0.0.0.0:5000/search_user', data=data)
    if r.text != "":
        try:
            jn = r.json()
        except:
            print('Not a valid JSON')
        id = jn.get('id')
        name = jn.get('name')
    elif r.text == "" or id is None or name is None:
        print('No result')
    else:
        print('[{}] {}'.format(id, name))
