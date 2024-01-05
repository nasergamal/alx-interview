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
            if byte_count > 4:
                return False
        else:
            if not (i & (1 << 7) and not (i & 1 << 6)):
                return False
        byte_count -= 1
    return byte_count == 0
