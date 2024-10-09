# INT_TO_CHAR = {
#     0: '0',
#     1: '1',
#     2: '2',
#     3: '3',
#     4: '4',
#     5: '5',
#     6: '6',
#     7: '7',
#     8: '8',
#     9: '9',
# }

# def integer_to_string(number):
#     if number == 0:
#         return '0'

#     digits = []
#     while number > 0:
#         digits.append(number % 10)
#         number //= 10

#     digits = digits[::-1]
#     chars = ''
#     for digit in digits:
#         chars += INT_TO_CHAR[digit]
#     return chars

DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def integer_to_string(number):
    result = ""

    while number > 0:
        number, remainder = divmod(number, 10)
        result = DIGITS[remainder] + result

    return result or "0"

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True
