MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24


def time_of_day(distance):
    distance = distance % (MINUTES_PER_HOUR * HOURS_PER_DAY)
    hour = distance // MINUTES_PER_HOUR
    minute = distance - (hour * MINUTES_PER_HOUR)
    return f'{hour:02d}:{minute:02d}'
    
print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True
