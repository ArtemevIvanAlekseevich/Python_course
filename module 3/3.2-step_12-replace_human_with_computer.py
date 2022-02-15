import sys
import re

def replace_human_with_computer():
    for line in sys.stdin:
        line = line.rstrip()
        # process line
        pattern = "human"
        print(re.sub(pattern, "computer", line))
        

if __name__ == "__main__":
    replace_human_with_computer()