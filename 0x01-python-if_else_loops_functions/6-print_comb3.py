#!/usr/bin/python3
for alpha in range(9):
    for alpha2 in range(10):
        if alpha == alpha2:
            continue
        else:
            if alpha == 8 and alpha2 == 9:
                print("{}{}".format(alpha, alpha2))
            else:
                print("{}{}, ".format(alpha, alpha2), end='')
