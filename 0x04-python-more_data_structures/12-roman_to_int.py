#!/usr/bin/python3
def roman_to_int(roman_string):
    value = 0
    roman_dic = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
    if roman_string:
        for idx in range(len(roman_string)):
            if (idx + 1 < len(roman_string)):
                if (roman_dic[roman_string[idx]] < roman_dic[roman_string[idx +1]]):
                    value -= roman_dic[roman_string[idx]]
                    continue
            value += roman_dic[roman_string[idx]]
        return value
    else:
        return None
