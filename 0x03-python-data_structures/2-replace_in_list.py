#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if (idx < 0 || idx > len(my_list)):
        return my_list
    for i in range(idx):
        my_list[i] = element
