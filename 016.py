n = 1000

number = 2 ** n
num_str = str(number)
sum = 0
for i in range(0, len(num_str)):
    sum += int(num_str[i])

print sum