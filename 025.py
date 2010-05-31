x = 1
y = 1
t = 1

while True:
    num_str = str(x)
    if len(num_str) == 1000:
        print t, x
        exit()
    temp = y
    y = x + y
    x = temp
    t += 1
