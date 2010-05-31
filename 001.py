total = 0
for x in range(3,1000):
    if x % 3 == 0 or x % 5 == 0:
        total += x
print total

# or

total = 0
for x in range(1, 334):
    total += 3 * x
for x in range(1, 200):
    total += 5 * x
for x in range(1, 67):
    total -= 15 * x
print total