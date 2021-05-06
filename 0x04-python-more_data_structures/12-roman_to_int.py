#!/usr/bin/python3
def roman_to_int(roman_string):
    value = 0
    if roman_string:
        for letter in roman_string:
            if letter < letter -1:
                if letter == "I": value += 1
                if letter == "V": value += 5
                if letter == "X": value += 10
                if letter == "L": value += 50
                if letter == "C": value += 100
                if letter == "D": value += 500
                if letter == "M": value += 1000
            else:
                if letter == "I": value -= 1
                if letter == "V": value -= 5
                if letter == "X": value -= 10
                if letter == "L": value -= 50
                if letter == "C": value -= 100
                if letter == "D": value -= 500
                if letter == "M": value -= 1000
        return value
    else:
        return None
