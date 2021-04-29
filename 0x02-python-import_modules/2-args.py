#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv) - 1
    if argc == 0:
        print("0 arguments.")
    elif (argc == 1):
        print("1 argument:\n 1: {}".format(argv))
    else:
        print("{} arguments:".format(argc))
        for count in range(1, argc):
            print("{}: {}".format(count, argv[count]))
