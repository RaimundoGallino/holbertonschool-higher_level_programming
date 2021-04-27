#!/usr/bin/python3
for letter_alphabet in range(ord('a'), ord('z')+1):
    if chr(letter_alphabet) not in "qe":
        print(chr(letter_alphabet), end='')
