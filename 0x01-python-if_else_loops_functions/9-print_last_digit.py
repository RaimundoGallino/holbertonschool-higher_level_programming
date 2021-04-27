#!/usr/bin/python3
def print_last_digit(number):
    if number > 9:
        print("{}".format(number % 10))
    else:
        print("{}".format(number))
