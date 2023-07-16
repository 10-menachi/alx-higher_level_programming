#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics:
"""

import sys
from collections import defaultdict


def print_statistics(total_file_size, status_code_counts):
    """
    Print statistics
    """
    print("File size:", total_file_size)
    for status_code in sorted(status_code_counts.keys()):
        count = status_code_counts[status_code]
        print(f"{status_code}: {count}")


def parse_line(line):
    """
    Parse a line from stdin
    """
    parts = line.split()
    if len(parts) >= 9:
        return int(parts[-1])
    return 0


def compute_metrics():
    """
    Compute metrics
    """
    total_file_size = 0
    status_code_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            file_size = parse_line(line)
            total_file_size += file_size

            status_code = line.split()[8]
            status_code_counts[status_code] += 1

            if line_count % 10 == 0:
                print_statistics(total_file_size, status_code_counts)
                print()

    except KeyboardInterrupt:
        print_statistics(total_file_size, status_code_counts)


compute_metrics()
