#!/bin/bash
#Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl "$1" -s | grep "Allow" | cut -d " " -f2
