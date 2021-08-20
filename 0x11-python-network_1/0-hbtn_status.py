#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""


import urllib.request


if __name__ == "__main__":

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        resp = response.read()
        print("Body response:")
        print("\t- type: " + str(type(resp)))
        print("\t- content: " + str(resp))
        print("\t- utf-8 content: " + str(resp.decode('utf-8')))
