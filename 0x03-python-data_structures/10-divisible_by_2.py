#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    boolean = []

    for element in my_list:
        if (element % 2 == 0):
            boolean.append(True)
        else:
            boolean.append(False)
    return (boolean)
