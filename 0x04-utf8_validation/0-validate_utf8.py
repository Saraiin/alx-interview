#!/usr/bin/python3
"""UTF-8 Validation"""


def count_starting_bits(byte):
    count = 0
    while byte & (1 << (7 - count)):
        count += 1
    return count


def validUTF8(data):
    i = 0
    while i < len(data):
        start_bits = count_starting_bits(data[i])

        if start_bits == 0:
            i += 1
        elif start_bits == 1 or start_bits > 4:
            return False
        else:
            for j in range(1, start_bits):
                if i + j >= len(data) or (data[i + j] & 0b11000000) != 0b10000000:
                    return False
            i += start_bits

    return True
