def dif_obj():
    objects = [1, 2, 3, 4, 1, 1, 2, [1], [1]]
    ans = 0
    s = []
    for i in objects:
        if id(i) not in s:
            ans += 1
            s.append(id(i))
    print(ans)

if __name__ == "__main__":
    dif_obj()
    