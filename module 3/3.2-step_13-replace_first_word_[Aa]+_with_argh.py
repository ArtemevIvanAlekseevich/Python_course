import sys
import re

def replace_first_Aa_word_with_argh():
    for line in sys.stdin:
        line = line.rstrip()
        # process line
        pattern = r"\b[Aa]+\b"
        print(re.sub(pattern, "argh", line, count=1))
        

if __name__ == "__main__":
    replace_first_Aa_word_with_argh()