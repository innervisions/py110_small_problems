def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def is_real_palindrome(string: str) -> bool:
    chars = [char for char in string if char.isalnum()]
    fixed_string = ''.join(chars).casefold()
    return is_palindrome(fixed_string)


print(is_real_palindrome("madam") == True)  # True
print(is_real_palindrome("356653") == True)  # True
print(is_real_palindrome("356635") == False)  # True
print(is_real_palindrome("356a653") == True)  # True
print(is_real_palindrome("123ab321") == False)  # True

# case doesn't matter
print(is_real_palindrome("Madam") == True)  # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True)  # True
