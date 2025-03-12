import sys


def process_file(file_path):
    with open(file_path, 'r') as f:
        line = f.readline().strip()
        a, b, c = map(float, line.split())
        if a == 0:
            print("Error. a cannot be 0")
            sys.exit(1)
        return a, b, c
