import sys
import re

def replace_all_identical_letters_with_one():
    pattern = r"(\w)\1{1,}"
    for line in sys.stdin:
        line = line.rstrip()
        # process line
        ans = line
        while re.search(pattern, ans) is not None:
            repeated_letters = re.search(pattern, ans)
            ans = ans[:repeated_letters.start()+1] + ans[repeated_letters.end():]
        print(ans)  

if __name__ == "__main__":
    replace_all_identical_letters_with_one()
    