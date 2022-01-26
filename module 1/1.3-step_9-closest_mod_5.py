def closest_mod_5(x):
    for i in range (5):
        if (x + i) % 5 == 0:
            a = x + i
            print(a)
            return a
    
    
if __name__ == "__main__":
    closest_mod_5(int(input()))
