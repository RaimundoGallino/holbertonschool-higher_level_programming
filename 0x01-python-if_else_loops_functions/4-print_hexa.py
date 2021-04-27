#!/usr/bin/python3
for alpha in range(0, 98):
    print("{:d} =".format(alpha), end='')
    print("0x{:d}".format(alpha % 16))
