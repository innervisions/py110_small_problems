def leading_substrings(string):
    return [string[: idx + 1] for idx in range(len(string))]


def substrings(string):
    result = []
    for idx in range(len(string)):
        result.extend(leading_substrings(string[idx:]))
    return result

def is_palindrome(string):
    return len(string) > 1 and string == string[::-1]

def palindromes(string):
    return [substring
            for substring in substrings(string)
            if is_palindrome(substring)]


print(palindromes("abcd") == [])  # True
print(palindromes("madam") == ["madam", "ada"])  # True

print(
    palindromes("hello-madam-did-madam-goodbye")
    == [
        "ll",
        "-madam-",
        "-madam-did-madam-",
        "madam",
        "madam-did-madam",
        "ada",
        "adam-did-mada",
        "dam-did-mad",
        "am-did-ma",
        "m-did-m",
        "-did-",
        "did",
        "-madam-",
        "madam",
        "ada",
        "oo",
    ]
)  # True

print(
    palindromes("knitting cassettes")
    == [
        "nittin",
        "itti",
        "tt",
        "ss",
        "settes",
        "ette",
        "tt",
    ]
)  # True
