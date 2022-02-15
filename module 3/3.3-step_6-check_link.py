import requests
import re

def check_link(url_parent, url_child):
    pattern = r"href=\"(.*)\""
    res = requests.get(url_parent)
    if res.status_code == 200:
        all_inclusions = re.findall(pattern, res.text)
    else:
        print("No")
        return
    for link in all_inclusions:
        res = requests.get(link)
        if res.status_code == 200:
            all_inclusions_this_page = re.findall(pattern, res.text)
            if url_child in all_inclusions_this_page:
                print("Yes")
                return
    print("No")
    return

if __name__ == "__main__":
    check_link(input(), input())