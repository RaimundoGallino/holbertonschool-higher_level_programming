#!/usr/bin/python3
for letter_alphabet in range(ord('z'), ord('a'), -1):
    if letter_alphabet % 2 != 0:
        letter_alphabet = letter_alphabet - 32
    print("{:c}" .format(letter_alphabet), end="")
