#!/usr/bin/python3
"""
Deviding a matrix by a selected div
"""

def matrix_divided(matrix, div):
    """Error prouf function"""

    if isinstance(div, int) is False and isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if isinstance(matrix, list) is False:
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    for i in range(len(matrix)):
        if isinstance(matrix[i], list) is False:
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            if isinstance(matrix[i][j], (int, float)) is False:
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    return list(map(lambda x: list(map(lambda y: \
round((y / div), 2), x)), matrix))
