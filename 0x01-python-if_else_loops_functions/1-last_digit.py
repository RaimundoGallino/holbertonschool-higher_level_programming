#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = 0
if number < 0:
    last_digit = -number % 10
    last_digit *= -1
else last_digit
    last_digit = number % 10
if last_digit < 6:
    print("Last digit of {:d}".format(number), end='')
    print("is {:d}".format(last_digit), end='')
    print("and is less than 6 and not 0")
if last_digit% 10 == 0:
    print("Last digit of {:d}".format(number), end='')
    print("is {:d}".format(last_digit), end='')
    print("and is 0")
if last_digit % 10 > 5:
    print("Last digit of {:d}".format(number), end='')
    print("is {:d}".format(last_digit), end='')
    print("and is greater than 5")
