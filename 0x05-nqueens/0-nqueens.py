#!/usr/bin/python3
'''return possible queens placements'''
import sys


def queens(n, i, a, b, c):
    '''
    generator that check possible placements
    n: board size n*n
    i: current piece
    a: current placements
    b: diagonal
    c: anti diagonal
    '''
    if i < n:
        for j in range(n):
            if j not in a and i+j not in b and i-j not in c:
                yield from queens(n, i+1, a+[j], b+[i+j], c+[i-j])
    else:
        yield list(zip(range(n), a))


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
elif not(sys.argv[1]).isdigit():
    print("N must be a number")
    sys.exit(1)
digit = int(sys.argv[1])
if digit < 4:
    print("N must be at least 4")
    sys.exit(1)
for solution in queens(digit, 0, [], [], []):
    print(solution)
