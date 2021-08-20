#!/bin/bash
#Bash script that takes in a URL, sends a POST request to the passed URL
curl "$1" -s -H -X POST -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD"
