def time_difference(time1, time2):
    '''This function takes in days, hours, minutes, and seconds from two days and determines how far apart the two days are.'''
    day = 86400   # 60 * 60 * 24
    hour = 3600   # 60 * 60
    minute = 60   # 60
    second = 1    # 1

    seconds1 = 0
    seconds1 += (time1[0] * day) + (time1[1] * hour) + (time1[2] * minute) + time1[3] 

    seconds2 = 0
    seconds2 += (time2[0] * day) + (time2[1] * hour) + (time2[2] * minute) + time2[3]

    difference = seconds2 - seconds1

    day_diff = int(difference / day)
    difference %= day

    hour_diff = int(difference / hour)
    difference %= hour

    min_diff = int(difference / minute)
    difference %= minute

    sec_diff = int(difference / second)
    difference %= second

    return day_diff, hour_diff, min_diff, sec_diff


print(time_difference([1, 0, 0, 0], [2, 3, 4, 5]))
print(time_difference([5, 3, 23, 22], [24, 4, 20, 45]))