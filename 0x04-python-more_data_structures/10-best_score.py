#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary.items():
        return max(a_dictionary)
    else:
        return a_dictionary
