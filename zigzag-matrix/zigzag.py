"""
Print a 2D array in zigzag pattern.
Even rows (0, 2, 4...) are printed left to right.
Odd rows (1, 3, 5...) are printed right to left.

Example:
    Input: [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]]
    Output: 1, 2, 3, 4, 8, 7, 6, 5, 9, 10, 11, 12

Args:
    array: 2D list to traverse in zigzag pattern

Returns the values as a list, so the tests can check it.
"""


def printZigZag(array):
    result = []
    for index, item in enumerate(array):
        if index % 2 !=0:
            result += item[::-1]
        else:
            result += item


    return result
