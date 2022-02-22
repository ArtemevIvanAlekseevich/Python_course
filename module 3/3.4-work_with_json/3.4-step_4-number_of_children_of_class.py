import json

def main():
    json_obj = input()       
    ans = {}
    all_ancestors = {}
    ans_lst = []
    data = json.loads(json_obj)
    for obj in data:
        all_ancestors[obj["name"]] = obj["parents"]
    for key in all_ancestors: 
        find_all_parents(key, all_ancestors)
    for key in all_ancestors:
        ans[key] = [key]
        for keys in all_ancestors:
            if key in all_ancestors[keys]:
                ans[key].append(keys)
    for key in ans:
        s = f'{key} : {len(ans[key])}'
        ans_lst.append(s)
    ans_lst.sort()
    for line in ans_lst:
        print(line)

def find_all_parents(name, all_ancestors):
    for parent in all_ancestors[name]: 
        for grant in all_ancestors[parent]:
            find_all_parents(parent, all_ancestors)
            if grant not in all_ancestors[name]:
                all_ancestors[name].append(grant)

if __name__ == "__main__":
    main()