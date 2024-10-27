import datetime

# def friday_the_13ths(year):
#     thirteenths = 0
#     for month in range(1, 13):
#         date = datetime.date(year, month, 13)
#         if date.weekday() == 4:
#             thirteenths += 1
#     return thirteenths


def friday_the_13ths(year):
    return len([month for month in range(1, 13)
                if datetime.date(year, month, 13).weekday() == 4])


print(friday_the_13ths(1986) == 1)  # True
print(friday_the_13ths(2015) == 3)  # True
print(friday_the_13ths(2017) == 2)  # True
