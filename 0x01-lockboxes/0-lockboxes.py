#!/usr/bin/python3
"""Check if all boxes (list of lists array where each element is a box
containing keys to other elements) are unlocked"""


def canUnlockAll(boxes):
    # Set to keep track of unlocked boxes
    unlocked_boxes = {0}

    # List to keep track of keys that can be used to unlock more boxes
    keys = boxes[0]

    # Continue until there are no more keys
    while keys:
        # Pop a key from the list
        key = keys.pop()

        # Check if the key corresponds to a valid box and has not been unlocked yet
        if key not in unlocked_boxes and key < len(boxes):
            # Add the newly unlocked box to the set of unlocked boxes
            unlocked_boxes.add(key)
            # Extend the list of keys with the keys in the newly unlocked box
            keys.extend(boxes[key])

    # Check if all boxes have been unlocked
    return len(unlocked_boxes) == len(boxes)
