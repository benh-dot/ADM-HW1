def is_leap(year):
    # divisible by 4, except centuries unless divisible by 400
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


year = int(input())
print(is_leap(year))
