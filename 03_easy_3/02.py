MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
MINUTES_PER_DAY = HOURS_PER_DAY * MINUTES_PER_HOUR

def after_midnight(time):
    hours = int(time[:2]) % 24
    minutes = int(time[3:])
    return (hours * MINUTES_PER_HOUR) + minutes


def before_midnight(time):
    return (MINUTES_PER_DAY - after_midnight(time)) % MINUTES_PER_DAY


print(after_midnight("00:00") == 0)  # True
print(before_midnight("00:00") == 0)  # True
print(after_midnight("12:34") == 754)  # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)  # True
print(before_midnight("24:00") == 0)  # True
