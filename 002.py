(x, y) = (1, 1)
total = 0
while y <= 4000000:
    if y % 2 == 0:
        total += y
    (x, y) = (y, x + y)

print total
