#!/usr/bin/python3
'''
    prime game challenge:
    Given a set of consecutive integers starting from 1 up to and including x.
    two players take turns choosing a prime number from the set and removing
    that number and its multiples from the set. The player that cannot make
    a move loses the game
'''


def isWinner(x, nums):
    '''
        calculate the winner
    '''
    if x < 1 or not nums:
        return None
    results = {'Ben': 0, 'Maria': 0}
    max_number = max(nums)
    primes = [True] * (max_number + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(max_number**0.5) + 1):
        if primes[i]:
            for n in range(i * i, max_number + 1, i):
                primes[n] = False
    for i in range(x):
        numbers = range(1, nums[i] + 1)

        found = False
        while(not found):
            for number in numbers:
                if primes[number]:
                    numbers = [num for num in numbers if num % number != 0]
                    found = True
                    break
            if not found:
                results['Ben'] = results['Ben'] + 1
                break

            found = False
            for number in numbers:
                if primes[number]:
                    numbers = [num for num in numbers if num % number != 0]
                    found = True
                    break
            if not found:
                results['Maria'] = results['Maria'] + 1
                break
            found = False
    if (results['Ben'] == results['Maria']):
        return None
    return max(results, key=lambda x: results[x])
