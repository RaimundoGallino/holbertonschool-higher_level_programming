#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request
to the URL and displays the body of the response (decoded in utf-8).
"""


import urllib.request
import urllib.error
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            log(fh, response.code, url)
    except urllib.error.HTTPError  as e:
        log(fh, e.code, url)

    with urllib.request.urlopen(argv[1]) as e:
        print (e)
