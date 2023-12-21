#!/usr/bin/env python3
"""
This module collects metrics for a web server.
"""

import sys

def print_stats(stats: dict, file_size: int) -> None:
    """Prints server metrics"""
    print(f"File size: {file_size}")
    for code, count in sorted(stats.items()):
        if count:
            print(f"{code}: {count}")

def compute_metrics():
    """Computes metrics for a web server"""
    file_size, count = 0, 0
    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    metrics = {code: 0 for code in status_codes}

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in metrics:
                    metrics[status_code] += 1
            except IndexError:
                pass
            try:
                file_size += int(data[-1])
            except (IndexError, ValueError):
                pass
            if count % 10 == 0:
                print_stats(metrics, file_size)
        print_stats(metrics, file_size)
    except KeyboardInterrupt:
        print_stats(metrics, file_size)
        raise

if __name__ == "__main__":
    compute_metrics()
