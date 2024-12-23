def leading_substrings(string):
    return [string[:idx + 1] for idx in range(len(string))]

def substrings(string):
    result = []
    for idx in range(len(string)):
        result.extend(leading_substrings(string[idx:]))
    return result
    
expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True
