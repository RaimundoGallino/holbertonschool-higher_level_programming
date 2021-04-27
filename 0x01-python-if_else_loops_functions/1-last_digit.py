#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number % 10 < 6:
    print("Last digit of {:d}".format(number), end='')
    print("is {:d}".format(number % 10), end='')
    print("and is less than 6 and not 0")
if number % 10 == 0:
    print("Last digit of {:d}".format(number), end='')
    print("is {:d}".format(number % 10), end='')
    print("and is 0")
if number % 10 > 5:
    print("Last digit of {:d}".format(number), end='')
    print("is {:d}".format(number % 10), end='')
    print("and is greater than 5")
