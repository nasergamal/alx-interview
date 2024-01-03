#!/usr/bin/python3
"""
UTF-8 Validation
"""
import chardet
from sys import getsizeof
byte = {'11110': 5, '1110': 4, '110': 3}


def validUTF8(data):
    byte_count = 0
    for i in data:
        if byte_count == 0:
            if i >> 7 > 1:
                return False
            for k, v in byte.items():
                if "{0:08b}".format(i)[:v] == k:
                    byte_count = v - 2
                    break
        else:
            if "{0:08b}".format(i)[:2] == '10':
                byte_count -= 1
            else:
                return False
    return byte_count == 0
