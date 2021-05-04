#!/usr/bin/python3
def element_at(my_list, idx):
    if (idx < 0 || idx > len(my_list)):
        return None
    print("Element at index {:d} is {:d}".format(idx, my_list[:idx]))
