import sys
import re

def find_double_cat():
    for line in sys.stdin:
        line = line.rstrip()
        # process line
        pattern = "cat.*cat"
        if re.search(pattern, line) is not None:
            print(line)

if __name__ == "__main__":
    find_double_cat()