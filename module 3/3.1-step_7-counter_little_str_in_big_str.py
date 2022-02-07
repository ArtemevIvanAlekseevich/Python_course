def counter_of_one_str_in_other():

    big_str = input()
    little_str = input()
    counter = 0
    for i in range(len(big_str)):
        if big_str.startswith(little_str, i):
            counter += 1
    return counter 

if __name__ == "__main__":
    print(counter_of_one_str_in_other())