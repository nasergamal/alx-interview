#!/usr/bin/python3
'''log parsing'''
import signal
from sys import stdin
i = 0
size = 0
possible = ['200', '301', '400', '401', '403', '404', '405', '500']
res = {}


def output(filesize, results):
    '''printing current stats'''
    print('File size:', filesize)
    for k, v in sorted(results.items()):
        print(f'{k}: {v}')


try:
    for line in stdin:
        content = line.split()
        if len(content) > 5:
            if content[-2] in possible:
                res[content[-2]] = res.get(content[-2], 0) + 1
            size += int(content[-1])
        i += 1
        if i == 10:
            output(size, res)
            i = 0
except Exception as e:
    pass
finally:
    output(size, res)
