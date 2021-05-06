#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[x*x for x in y] for y in matrix]
    return new_matrix
