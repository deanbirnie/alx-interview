#!/usr/bin/python3
"""This module provides a method which solves the lockboxes puzzle."""


def canUnlockAll(boxes):
    """
    This method returns true if all boxes can be unlocked, otherwise false
    """
    keys = [0]
    prev_key_len = 0
    while len(keys) > prev_key_len:
        prev_key_len = len(keys)
        for i in range(len(keys)):
            if keys[i] >= len(boxes):
                continue
            new_keys = boxes[keys[i]]
            for k in new_keys:
                if k not in keys:
                    keys.append(k)
    all_keys = list(range(len(boxes)))
    if all([key in keys for key in all_keys]):
        return True
    return False
