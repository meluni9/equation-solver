import sys


def process_file(file_path):
    try:
        with open(file_path, 'r') as f:
            line = f.readline().strip()
            a, b, c = map(float, line.split())
            if a == 0:
                print("Error. a cannot be 0")
                sys.exit(1)
            return a, b, c
    except FileNotFoundError:
        print(f"file {file_path} does not exist")
        sys.exit(1)
    except ValueError:
        print("invalid file format")
        sys.exit(1)
