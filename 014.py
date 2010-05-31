chain_lengths = { 1: 1 }

n = 999999

max_length = 0
max_start = 0

def get_chain_length(n):
    if n in chain_lengths:
        return chain_lengths[n]
    else:
        if n % 2 == 0:
            next = n / 2
        else:
            next = n * 3 + 1

        length = 1 + get_chain_length(next)
        chain_lengths[n] = length
        return length

while n > 0:
    if n % 1000 == 0:
        print n, max_length
    length = get_chain_length(n)
    if length > max_length:
        max_length = length
        max_start = n
    n -= 1

print max_start, max_length
