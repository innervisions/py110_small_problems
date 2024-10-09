CHAR_TO_INT = {
    '0': 0,
    '1': 1,
    '2': 2, 
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
}

def string_to_integer(number_string):
    multiplier = 1
    result = 0
    number_string = number_string[::-1]
    for char in number_string:
        num = CHAR_TO_INT[char]
        result += multiplier * num
        multiplier *= 10
    return result


print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True
