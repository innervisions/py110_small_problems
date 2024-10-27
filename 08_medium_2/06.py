def sum_square_difference(count):
    integers = list(range(1, count + 1))
    squares = [num**2 for num in integers]
    return sum(integers)**2 - sum(squares)

print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True
