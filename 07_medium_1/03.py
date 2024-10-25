def rotate_string(string):
    return string[1:] + string[0:1]

def rotate_rightmost_digits(digits, num_digits):
    new_digits = digits[0:len(digits) - num_digits] + rotate_string(digits[-num_digits:])
    return new_digits

def max_rotation(number):
    digits = str(number)
    for idx in range(len(digits), 1, -1):
        digits = rotate_rightmost_digits(digits, idx)
    return int(digits)


print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True
