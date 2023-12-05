#!/usr/bin/python3
"""This module provides a method which solves the lockboxes puzzle."""


def canUnlockAll(boxes):
    """This method returns true if all boxes can be unlocked, otherwise false"""
    unique_keys = [0]
    new_boxes_we_can_open = []
    i = 0
    for box in boxes:
        for key in box:
            if key:
                if key not in unique_keys:
                    unique_keys.append(key)
                    new_boxes_we_can_open.append(key)
        for box in new_boxes_we_can_open:
            new_keys = boxes[box]
            if new_keys:
                for key in new_keys:
                    if key not in unique_keys:
                        unique_keys.append(key)

        if i in unique_keys:
            i += 1
        else:
            return False

    return True
