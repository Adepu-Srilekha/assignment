def leap_year(year):
    if year%400 ==0:
        return True
    elif year % 100==0:
        return False
    elif year %4 ==0:
        return True
    else:
        return False

print(leap_year(2000))
print(leap_year(2021))
