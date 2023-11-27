#!/usr/bin/python3
"""
    Pascal triangle function
"""


def pascal_triangle(n):
    '''
    pascal triangle function's time complexity is O(n^2)
    '''
    triangle = []
    for i in range(n):
        row = []
        for n in range(i + 1):
            if n == 0 or n == i:
                row.append(1)
            elif n < i // 2 + 1:
                row.append(triangle[i - 1][n - 1] + triangle[i - 1][n])
            else:
                row.append(row[i - n])
        triangle.append(row)
    return triangle
