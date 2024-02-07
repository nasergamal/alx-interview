#!/usr/bin/python3
'''island perimeter challenge'''


def island_perimeter(grid):
    '''measure perimeter'''
    x, y = len(grid), len(grid[0])
    perimeter = 0
    for i in range(x):
        for n in range(y):
            if grid[i][n] == 1:
                perimeter += 4
                if i < x - 1 and grid[i + 1][n] == 1:
                    perimeter -= 2
                if n < y - 1 and grid[i][n + 1] == 1:
                    perimeter -= 2
    return perimeter
