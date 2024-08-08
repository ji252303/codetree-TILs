y, m, d = map(int,input().split())

def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def get_month(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if leap_year(year):
            return 29
        else:
            return 28
    else:
        return -1

def get_season(year, month, day):
    if month < 1 or month > 12:
        return -1
    
    days_month = get_month(year, month)
    if day < 1 or day > days_month:
        return -1

    if 3 <= month <= 5:
        return "Spring"
    elif 6 <= month <= 8:
        return "Summer"
    elif 9 <= month <= 11:
        return "Fall"
    else:
        return "Winter"


result = get_season(y,m,d)
print(result)