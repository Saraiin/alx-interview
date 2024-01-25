#!/usr/bin/python3
"""Parses log"""
import sys
import signal


def compute_metrics(lines):
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    for line in lines:
        try:
            # Splitting the line to extract relevant information
            parts = line.split()
            ip_address, date, method, status_code, file_size = parts[0], parts[3][1:], parts[5], int(parts[8]), int(parts[9])

            # Updating total file size
            total_size += file_size

            # Updating status code counts
            if status_code in status_counts:
                status_counts[status_code] += 1

        except (ValueError, IndexError):
            # Skip lines that do not match the expected format
            continue

    return total_size, status_counts

def print_metrics(total_size, status_counts):
    print(f'Total file size: {total_size}')

    for code in sorted(status_counts.keys()):
        count = status_counts[code]
        if count > 0:
            print(f'{code}: {count}')
