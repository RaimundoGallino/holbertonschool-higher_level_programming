#!/usr/bin/python3

def element_at(my_list, idx):
    if (idx < 0 || idx > len(my_list)):
        return None
    print("Element at index {} is {}".format(my_list[:idx]))
