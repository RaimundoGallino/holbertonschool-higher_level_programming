#!/usr/bin/python3
for letter_alphabet in range(ord('a'), ord('z'), -1):
    if letter_alphabet % 2 == 0:
        letter_alphabet = ord(letter_alphabet) - 32
    print("{:c}" .format(letter_alphabet))
