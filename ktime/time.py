def gmtime(secs=None):
    epoch = (1970, 1, 1, 0, 0, 0, 3, 1, 0)
    if secs == 0: # epoch
        return epoch
    result = list(epoch)
    remaining = secs
    leap_year_secs = 31622400

    def is_leap_year(year):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else: 
                    return False
            return True 
        else:
            return False

    def secs_this_year(year):
        if is_leap_year(year):
            return leap_year_secs
        else:
            return 31536000

    while ((remaining / leap_year_secs) >= 1):
        remaining = remaining - secs_this_year(result[0])
        result[0] += 1

    days = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def secs_this_month(year, month):
        if is_leap_year(year):
            days[1] = 29
        secs_this_month = 24 * 60 * 60 * days[month]
        return secs_this_month

    def secs_this_day(year, month, day):
        if is_leap_year(year):
            days[1] = 29
        assert (day-1) <= days[month]

        secs_this_day = 24 * 60 * 60
        return secs_this_day

    while remaining / secs_this_month(result[0], result[1]) >= 1:
        remaining = remaining - secs_this_month(result[0], result[1])
        result[7] += days[result[1]]
        result[1] += 1

    while remaining / secs_this_day(result[0], result[1], result[2]) >= 1:
        remaining = remaining - secs_this_day(result[0], result[1], result[2])
        result[2] += 1
        result[7] += 1

    result[6] = result[7] % 7
    return tuple(result)
