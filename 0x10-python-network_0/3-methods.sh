#!/bin/bash
#Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl "$1" -s -I | grep 'Allow' | cut -d ' ' -f 2-
