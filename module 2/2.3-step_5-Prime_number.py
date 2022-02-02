def primes():
    number = 1
    while True: 
        number += 1
        a = 0
        for i in range(1, number):
            if number % i == 0:
                a += 1
        if a == 1:
            yield number

        
