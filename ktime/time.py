def gmtime(secs=None):
    epoch = (1970, 1, 1, 0, 0, 0, 3, 1, 0)
    if secs == 0: # epoch
        return epoch
    result = list(epoch)
    remaining = secs
    LEAP_YEAR_SECS = 31622400
    NORMAL_YEAR_SECS = 31536000

    def is_leap_year(year):
        if year % 4 == 0:
            if year % 100 == 0 and year >= 2000:
                if year % 400 == 0:
                    return True
                else: 
                    return False
            return True 
        else:
            return False

    def secs_this_year(year):
        if is_leap_year(year):
            return LEAP_YEAR_SECS
        else:
            return NORMAL_YEAR_SECS

    while ((remaining / NORMAL_YEAR_SECS) >= 1):
        remaining -= secs_this_year(result[0])
        result[0] += 1

    days = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def secs_this_month(year, month):
        if is_leap_year(year):
            days[2] = 29
        secs_this_month = 24 * 60 * 60 * days[month]
        return secs_this_month

    SECS_THIS_DAY = 86400
    while remaining / secs_this_month(result[0], result[1]) >= 1:
        remaining -= secs_this_month(result[0], result[1])
        result[7] += days[result[1]]
        result[1] += 1

    while remaining / SECS_THIS_DAY >= 1:
        remaining -= SECS_THIS_DAY
        result[2] += 1
        result[7] += 1

    SECS_PER_HOUR = 3600
    while remaining / SECS_PER_HOUR >= 1:
        remaining -= SECS_PER_HOUR
        result[3] += 1

    SECS_PER_MIN = 60
    while remaining / SECS_PER_MIN >= 1:
        remaining -= SECS_PER_MIN
        result[4] += 1

    result[5] = int(remaining)
    remaining -= int(remaining)

    def day_of_week(y, m, d):
        """
        Ripped from https://en.wikipedia.org/wiki/Calculating_the_day_of_the_week
        and translated to Python"""
        t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
        y -= m < 3
        PYTHON_DAY_OF_WEEK_OFFSET = 6 # in original algorithm 0=Sunday
        return (y + y/4 - y/100 + y/400 + t[m-1] + d + PYTHON_DAY_OF_WEEK_OFFSET) % 7

    result[6] = day_of_week(result[0], result[1], result[2])

    return tuple(result)
