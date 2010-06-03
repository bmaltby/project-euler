
coin_values = [200, 100, 50, 20, 10, 5, 2, 1]
coin_index = 0

def count_perms(sum, coin_index):
    if coin_index >= len(coin_values):
        return 0
    perms = count_perms(sum, coin_index + 1)

    while sum >= coin_values[coin_index]:
        sum -= coin_values[coin_index]
        if sum == 0:
            perms += 1
        else:
            perms += count_perms(sum, coin_index + 1)

    return perms

print count_perms(200, 0)
