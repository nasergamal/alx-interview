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
            if ("{0:08b}".format(i)).startswith(tuple(byte)):
                for k, v in byte.items():
                    if "{0:08b}".format(i)[:v] in k:
                        byte_count = v - 2
                        break
            elif i >> 7 != 0:
                return False
        else:
            if "{0:08b}".format(i)[:2] != '10':
                return False
            byte_count -= 1
    return byte_count == 0
