def is_palindrome(string: str) -> bool:
    return string == string[::-1]

# All True
print(is_palindrome("madam") == True)
print(is_palindrome("356653") == True)
print(is_palindrome("356635") == False)

# case matters
print(is_palindrome("Madam") == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)
