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
    print result, remaining, secs_this_month(result[0], result[1]), is_leap_year(result[0])

    while remaining / SECS_THIS_DAY >= 1:
        print result, remaining, SECS_THIS_DAY
        remaining -= SECS_THIS_DAY
        result[2] += 1
        result[7] += 1

    result[6] = result[7] % 7
    return tuple(result)
