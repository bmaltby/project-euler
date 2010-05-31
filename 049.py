import itertools
n = 10000

prime_array = [True] * n
for i in xrange(2, int(n/2)):
    if prime_array[i]:
        j = i * 2
        while j < n:
            prime_array[j] = False
            j += i

primes = [ ]
for i in xrange(1000, n):
    if prime_array[i]:
        primes.append(i)

print 'generated primes'

num_primes = len(primes)
for i in xrange(0, num_primes - 2):
    a = primes[i]
    for j in range(i + 1, num_primes - 1):
        b = primes[j]
        diff = primes[j] - primes[i]
        c = b + diff
        if c < n and prime_array[c]:
            perms = [ ]
            for x in itertools.permutations(str(a)):
                perms.append(''.join(x))
            if str(b) in perms and str(c) in perms:
                print a, b, c
