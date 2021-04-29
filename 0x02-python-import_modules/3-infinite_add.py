#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv)
    sum = 0
    if (argc == 0):
        print("0")
    for count in range(1, argc):
        sum += int(argv[count])
    print("{}".format(sum))
