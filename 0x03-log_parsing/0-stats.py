import sys


file_sizes = []
status_code_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()

        if len(parts) >= 7 and parts[5].isdigit() and int(parts[5]) in status_code_count:
            file_size = int(parts[6])
            status_code = int(parts[5])

            file_sizes.append(file_size)
            status_code_count[status_code] += 1
            line_count += 1

        if line_count == 10:
            total_size = sum(file_sizes)
            print(f"File size: {total_size}")

            for code in sorted(status_code_count.keys()):
                count = status_code_count[code]
                if count > 0:
                    print(f"{code}: {count}")

            file_sizes = []
            status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
            line_count = 0

except KeyboardInterrupt:
    total_size = sum(file_sizes)
    pr
