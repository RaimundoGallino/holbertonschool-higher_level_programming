#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_of_unique_numbers = []
    unique_numbers = set(my_list)
    for number in unique_numbers:
        sum_of_unique_numbers += number
    return sum_of_unique_numbers
