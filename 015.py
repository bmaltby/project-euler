import math

n = 20

# at each step we either go right or down and we need to step n times in each direction
# hence we need to place n steps right into n out of n * 2 steps, thus we need (n*2) choose n

result = math.factorial(n * 2) / (math.factorial(n) * math.factorial((n*2) - n))
print result
