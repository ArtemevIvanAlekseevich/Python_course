import sys
import re

def find_str_with_tandem_repetition():
    for line in sys.stdin:
        line = line.rstrip()
        # process line
        pattern = r"\b(.+)\1\b"
        if re.search(pattern, line) is not None:
            print(line)

if __name__ == "__main__":
    find_str_with_tandem_repetition()