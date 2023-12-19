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
        try:
            if content[7] in possible:
                res[content[7]] = res.get(content[7], 0) + 1
                size += int(content[8])
        except IndexError:
            pass
        i += 1
        if i == 10:
            output(size, res)
            i = 0
except KeyboardInterrupt:
    pass
finally:
    output(size, res)
