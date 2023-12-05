#!/usr/bin/python3
"""This module provides a method which solves the lockboxes puzzle."""


def canUnlockAll(boxes):
    """
    This method returns true if all boxes can be unlocked, otherwise false
    """
    if (len(boxes) == 0):
        return True
    unique_keys = [0]
    new_boxes_we_can_open = []
    i = 0
    if len(boxes) <= 1 or boxes == [[]]:
        return True
    for box in boxes:
        if i not in unique_keys:
            return False
        for key in box:
            if key:
                if key not in unique_keys and key < len(boxes):
                    unique_keys.append(key)
                    new_boxes_we_can_open.append(key)
        for box2 in new_boxes_we_can_open:
            if boxes[box2]:
                new_keys = boxes[box2]
                if new_keys:
                    for key in new_keys:
                        if key not in unique_keys:
                            unique_keys.append(key)

        i += 1
    return True
