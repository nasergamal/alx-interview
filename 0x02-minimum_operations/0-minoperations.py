#!/usr/bin/python3
'''Measure the minimun number of operations required'''


def minOperations(n):
    '''
    minOperations return the minimum number of operations required
    to get exactly n*x characters using only Copy All and Paste
    operations
    '''
    if not n or type(n) != int:
        return 0
    x, i = n, 2
    op = 0
    while i <= x:
        while x % i == 0:
            op += i
            x //= i
        i += 1
    return op
