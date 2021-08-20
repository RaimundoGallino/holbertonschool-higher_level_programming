#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request
to the URL and displays the body of the response (decoded in utf-8).
"""


import requests
from sys import argv


if __name__ == "__main__":

    token = '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'
    owner = argv[1]
    repo = argv[2]
    query_url = f"https://api.github.com/repos/{owner}/{repo}"
    params = {
        "state": "open",
    }
    headers = {'Authorization': f'token {token}'}
    r = requests.get(query_url, headers=headers, params=params)
    print(r.json()['id'])
