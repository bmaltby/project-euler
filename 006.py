sum_squares = 0
square_sum = 0
n = 100

for i in range(0, n+1):
    sum_squares += i * i
    square_sum += i

square_sum = square_sum * square_sum

print square_sum - sum_squares