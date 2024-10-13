# def staggered_case(string:str):
#     result = ''
#     upper = True
#     for char in string:
#         if not char.isalpha():
#             result += char
#             continue
#         if upper:
#             result += char.upper()
#         else:
#             result += char.lower()
#         upper = not upper
#     return result


def staggered_case(string):
    result = ""
    upper = True

    for char in string:
        if char.isalpha():
            result += char.upper() if upper else char.lower()
            upper = not upper
        else:
            result += char

    return result


string = "I Love Launch School!"
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = "ALL_CAPS"
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = "ignore 77 the 4444 numbers"
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case("") == "")  # True
