#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        aux = str[:n] + str[n + 1:]
        return aux
    else:
        return str
