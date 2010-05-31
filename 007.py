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
            if n % i == 0:
                primes[n] = False
                return False
        primes[n] = True
        prime_list.append(n)
        return True


prime_index = 10001
i = 0
n = 0

while (True):
    if is_prime(i):
        n += 1
        if n == prime_index:
            print i
            exit()
    i += 1
