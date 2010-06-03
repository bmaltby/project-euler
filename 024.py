import itertools

i = 0
for p in itertools.permutations('0123456789'):
    i += 1
    if i == 1000000:
        print ''.join(p)
        exit()
