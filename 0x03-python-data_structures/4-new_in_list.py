#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    if (idx < 0 or idx > len(my_list)):
        return new_list
    for i in range(idx):
        new_list[i] = element

    return new_list
