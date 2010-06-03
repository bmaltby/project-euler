# 1 Jan 1900 is Monday so 7th Jan 1900 is a sunday

days_in_month = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

leap_years = {}
year = 1900
while year < 2001:
    if (year % 4 == 0) and not (year % 100 == 0 and year % 400):
        leap_years[year] = True
    else:
        leap_years[year] = False
    year += 1

year = 1900
month = 1
day = 7
sundays = 0

while year < 2001:
    day += 7
    daysformonth = days_in_month[month]
    if month == 2 and leap_years[year]:
        daysformonth = 29
    if day > daysformonth:
        day -= daysformonth
        month += 1
        if month > 12:
            month = 1
            year += 1
            if year == 2001:
                print sundays
                exit()
    if day == 1 and year > 1900:
        sundays += 1
