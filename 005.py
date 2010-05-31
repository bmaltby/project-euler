print 232792560

# or

limit = 20
m = 1
primes = [ ]
for i in range(2, limit + 1):
    for p in primes:
        if i % p == 0:
            break
    else:
        primes.append(i)
        p = i
        while p <= limit:
            m *= i
            p *= i

print m
