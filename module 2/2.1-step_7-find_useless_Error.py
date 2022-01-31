def family(n):
    
    for i in range(n):
        req = input().split()
        d[req[0]] = []
        for j in range (len(req) - 2):
            d[req[0]].append(req[j + 2])

def releation(parent, son):
    
    global l
    if parent == son:
        l += 1
    if d[son] == [] or l > 0:
        return
    if parent in d[son]:
        l += 1   
    for i in d[son]:
        releation(parent, i)

d = {}
n = int(input())
family(n)
l = 0
ans = []
previous_errors = []
for i in range(int(input())):
    l = 0
    req = input()
    for j in previous_errors:
        releation(j, req)
        if l > 0:
            ans.append(req)
            break
    previous_errors.append(req)

for i in ans:
    print(i)





