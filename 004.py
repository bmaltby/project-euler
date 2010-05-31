max = 0
for x in range(999,1, -1):
    if x * 999 < max:
        break
    for y in range(999,x - 1, -1):
        m = x * y
        s = str(m)
        if s == s[::-1] and m > max:
            max = m
print max
