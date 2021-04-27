#!/usr/bin/python3
for alpha in range(100):
    if alpha < 99:
        print("{:02d}, ".format(alpha), end='')
    else:
        print("{:02d}, ".format(alpha))
