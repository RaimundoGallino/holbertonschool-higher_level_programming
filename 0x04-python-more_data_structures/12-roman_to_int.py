#!/usr/bin/python3
def roman_to_int(roman_string):
    value = 0
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string:
        for idx in range(len(roman_string)):
            if (idx + 1 < len(roman_string)):
                if (dic[roman_string[idx]] < dic[roman_string[idx + 1]]):
                    value -= dic[roman_string[idx]]
                    continue
            value += dic[roman_string[idx]]
        return value
    else:
        return None
