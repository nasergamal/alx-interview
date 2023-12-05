#!/usr/bin/python3
'''check if all box can be unlocked'''


def canUnlockAll(boxes):
    '''
       boxes list of lists: boxes that contain 0 or more keys
    '''
    keys = [0]
    i = 0
    boxes_count = len(boxes) - 1
    while i < len(keys):
        if keys[i] > boxes_count:
            i += 1
            continue
        for key in boxes[keys[i]]:
            if key not in keys:
                keys.append(key)
        i += 1
    if all(key in keys for key in range(boxes_count + 1)):
        return True
    return False
