
n = 1000000

prime_array = [True] * n
for i in xrange(2, int(n/2)):
    if prime_array[i]:
        j = i * 2
        while j < n:
            prime_array[j] = False
            j += i

primes = [ ]
for i in xrange(2, n):
    if prime_array[i]:
        primes.append(i)

print 'generated primes'

longest_chain = 0
result = 0

num_primes = len(primes)
for i in xrange(0, num_primes):
    current_sum = primes[i]
    chain_length = 1
    for j in range(i + 1, num_primes):
        current_sum += primes[j]
        chain_length += 1
        if current_sum >= n:
            break
        if chain_length > longest_chain and prime_array[current_sum]:
            longest_chain = chain_length
            result = current_sum

print longest_chain
print result