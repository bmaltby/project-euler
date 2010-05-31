primes = { 2: True }
prime_list = [ 2 ]
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    if n in primes:
        return primes[n]
    else:
        for i in prime_list:
            if i > n / 2:
                primes[n] = True
                prime_list.append(n)
                return True
            if n % i == 0:
                primes[n] = False
                return False
        primes[n] = True
        prime_list.append(n)
        return True

i = 0
sum = 0
n = 2000000

#for i in range(0, n):
#    if is_prime(i):
#        sum += i

print sum


# alternative
sum = 0
prime_array = [True] * n
for i in range(2, int(n/2)):
    if prime_array[i]:
        j = i * 2
        while j < n:
            prime_array[j] = False
            j += i

for i in range(2, n):
    if prime_array[i]:
        sum += i

print sum