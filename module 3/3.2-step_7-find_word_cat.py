import sys
import re

def find_word_cat():
    for line in sys.stdin:
        line = line.rstrip()
        # process line
        pattern = r"\bcat\b"
        if re.search(pattern, line) is not None:
            print(line)

if __name__ == "__main__":
    find_word_cat()