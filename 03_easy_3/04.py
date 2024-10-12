def is_consonant(char):
    return char.isalpha() and char.casefold() not in 'aeiou'

def double_consonants(string):
    result = ''
    for char in string:
        result += char
        if is_consonant(char):
            result += char
    return result

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")
