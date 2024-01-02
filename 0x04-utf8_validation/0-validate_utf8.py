#!/usr/bin/python3
"""
UTF-8 Validation
"""
import chardet
from sys import getsizeof


def validUTF8(data):
    valid = []
    for i in data:
        if i.bit_length() > 8:
            return False
    return True
