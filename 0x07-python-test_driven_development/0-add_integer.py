#!/usr/bin/python3
if __name__ == "__main__":
    def add_integer(a, b=98):
        if isinstance(a, float): a = int(a)
        if isinstance(b, float): b = int(b)
        if isinstance(a, int) is False:
            raise TypeError("a must be an integer")
        elif isinstance(b, int) is False:
            raise TypeError("b must be an integer")
        else:
            return a + b
