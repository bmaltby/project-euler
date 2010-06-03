# define some groups

# letters for one, two to nine
digits = 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4
# ten to nineteen
teens = 3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8
# tens from twenty - ninety
tens = 6 + 6 + 5 + 5 + 5 + 7 + 6 + 6
# numbers in each hundred
perhundred = teens + (tens * 10) + (digits * 9)

answer = (digits * 100) + (900 * 7) + (891 * 3) + (10 * perhundred) + (3 + 8)

print answer