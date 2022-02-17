import requests
import re

def find_domain(url):
    pattern = r'<a.*?href=".*?:\/\/((?:\w|-)+(?:\.(?:\w|-)+)+)'
    res = requests.get(url)
    tex = res.text
    all_inclusions = re.findall(pattern, tex)
    ans = []
    for domains in all_inclusions:
        if domains not in ans:
            ans.append(domains)
    ans.sort()
    for i in ans:
        print(i)

if __name__ == "__main__":
    find_domain(input().strip())