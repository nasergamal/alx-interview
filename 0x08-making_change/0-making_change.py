#!/usr/bin/python3
'''minimum amount of coins'''


def makeChange(coins, total):
    '''calculate coins'''
    if total <= 0:
        return 0
    num = 0
    coins.sort(reverse=True)
    for coin in coins:
        while total >= coin:
            num += 1
            total -= coin
    if total == 0:
        return num
    return -1
