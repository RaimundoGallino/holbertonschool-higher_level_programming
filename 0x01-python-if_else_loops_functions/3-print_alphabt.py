#!/usr/bin/python3
for letter_alphabet in range(ord('a'), ord('z')+1):
    letter = chr(letter_alphabet)
    if letter not in "qe":
        print(letter, end="")
