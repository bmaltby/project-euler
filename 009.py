import math

a = 1
b = 0

while True:
    while b < a:
        b += 1
        c_sqr = (a * a) + (b * b)
        c = math.sqrt(c_sqr)
        if math.fmod(c, 1) == 0:
            c = int(c)
            print a, b, c
            if a + b + c == 1000:
                print a * b * c
                exit()
    a += 1
    b = 0