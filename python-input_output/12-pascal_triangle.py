#!/usr/bin/python3
"""Create a function def pascal_triangle(n):
that returns a list of lists of integers
representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """defain a function"""

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]

        row = [1]

        for j in range(1, len(prev_row)):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)
        triangle.append(row)

    return triangle
