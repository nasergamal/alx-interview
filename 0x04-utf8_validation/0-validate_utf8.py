#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    byte_count = 0
    for i in data:
        c = 1 << 7
        if byte_count == 0:
            while c & i:
                c >>= 1
                byte_count += 1
            if byte_count == 0:
                continue
        else:
            if not (i & 1 << 7):
                return False
        byte_count -= 1
    return byte_count == 0
