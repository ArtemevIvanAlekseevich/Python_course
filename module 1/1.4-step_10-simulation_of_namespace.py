def main():
    def create(nspace, parent):
        nonlocal d
        d[nspace] = [parent]
        d[parent].append(nspace)

    def add(nspace, var):
        nonlocal d
        d[nspace].append(var)

    def get(nspace, var):
        nonlocal d
        while nspace != 'global':
            if var in d[nspace]:
                return nspace
            else:
                nspace = d[nspace][0]
        if var in d[nspace]:
            return nspace
        return 'None'
            

    d = {'global': [0]}
    n = int(input())
    for i in range(n):
        request = input().split()
        if request[0] == 'create':
            create(request[1], request[2])
        elif request[0] == 'add':
            add(request[1], request[2])
        else:
            print(get(request[1], request[2]))

if __name__ == "__main__":
    main()