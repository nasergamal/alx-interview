#!/usr/bin/python3
'''check if all box can be unlocked'''


def canUnlockAll(boxes):
    '''
       boxes list of lists: boxes that contain 0 or more keys
    '''
    keys = {0}
    i = 0
    while i < len(keys):
        keys.update(boxes[i])
        i += 1
    if all(key in keys for key in range(len(boxes) - 1)):
        return True
    return False
