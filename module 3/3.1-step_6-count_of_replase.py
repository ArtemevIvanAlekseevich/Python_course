def counter_of_replace():

    s = input()
    a = input()
    b = input()
    counter = 0
    while a in s:
        s = s.replace(a, b)
        counter += 1
        if counter > 1000:
            return 'Impossible'
    return counter

if __name__ == "__main__":
    print(counter_of_replace())