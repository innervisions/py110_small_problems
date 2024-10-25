def rotate_string(string):
    return string[1:] + string[0:1]

def rotate_rightmost_digits(value, num_digits):
    digits = str(value)
    new_digits = digits[0:len(digits) - num_digits] + rotate_string(digits[-num_digits:])
    return int(new_digits)

print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)  # True
