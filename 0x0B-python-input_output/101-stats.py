import sys
import signal

total_file_size = 0
status_codes_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_statistics():
    print(f"Total file size: {total_file_size}")
    for status_code in sorted(status_codes_count.keys()):
        count = status_codes_count[status_code]
        if count > 0:
            print(f"{status_code}: {count}")

def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line = line.strip()
        if line:
            _, _, _, _, status_code, file_size = line.split()[0:6]
            total_file_size += int(file_size)
            status_codes_count[int(status_code)] += 1

            line_count += 1
            if line_count % 10 == 0:
                print_statistics()

except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)
