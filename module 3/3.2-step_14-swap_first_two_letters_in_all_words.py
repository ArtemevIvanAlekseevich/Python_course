import sys
import re

from soupsieve import match

def swap_first_two_letters_in_all_words():
    for line in sys.stdin:
        line = line.rstrip()
        # process line
        pattern = r"\b\w+\w\b"
        all_inclusions = re.findall(pattern, line)
        dx = 0
        ans = line
        for word in all_inclusions:
            match_object = re.search(word, line)
            line = line.replace(word, "", 1)
            x = match_object.start() + dx
            ans = ans[:x] + word[1] + word[0] + ans[x+2:] 
            dx += len(word)
        print(ans)  

if __name__ == "__main__":
    swap_first_two_letters_in_all_words()