import math

max_divisors = 500
t = 1
i = 2

while True:
    t = t + i
    i += 1

    num_divisors = 2 # for 1 and t

    max = t
    n = 2
    while n < max:
        if t % n == 0:
            num_divisors += 2
            max = t / n - 1
        n += 1

    if num_divisors > max_divisors:
        print t
        exit()
