#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics.
"""

import sys
from collections import defaultdict


def print_statistics(total_file_size, status_code_counts):
    """
    Print statistics.
    """
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_code_counts.keys()):
        count = status_code_counts[status_code]
        print(f"{status_code}: {count}")


def parse_line(line):
    """
    Parse a line from stdin.
    """
    parts = line.split()
    if len(parts) >= 9:
        status_code = parts[-2]
        try:
            file_size = int(parts[-1])
            return file_size, status_code
        except ValueError:
            return 0, ''
    return 0, ''


def compute_metrics():
    """
    Compute metrics from stdin.
    """
    total_file_size = 0
    status_code_counts = defaultdict(int)

    try:
        for line in sys.stdin:
            file_size, status_code = parse_line(line)
            total_file_size += file_size

            if status_code and status_code.isdigit():
                status_code_counts[status_code] += 1

        print_statistics(total_file_size, status_code_counts)

    except KeyboardInterrupt:
        print_statistics(total_file_size, status_code_counts)


if __name__ == "__main__":
    compute_metrics()
