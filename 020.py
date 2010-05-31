n = 100

number = 1
while n:
    number = n * number
    n -= 1

num_str = str(number)
sum = 0
for i in range(0, len(num_str)):
    sum += int(num_str[i])

print sum