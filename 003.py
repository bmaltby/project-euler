import math

def prime(p):
    for x in range(2, p):
        if p % x == 0:
            return False
    return True

x = 2
y = 600851475143
while x < y:
    if prime(x):
        while y % x == 0:
            y = y/x
    x += 1
print y

# or

x = 2
y = 600851475143
while (x != y):
    if y % x == 0:
        y = y / x
    else:
        x += 1
print x

