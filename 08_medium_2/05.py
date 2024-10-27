
def is_featured(number):
    return (
        number % 2 == 1 and
        number % 7 == 0 and
        len(str(number)) == len(set(str(number)))
    )

def next_featured(number):
    if number >= 9876543201:
        return "There is no possible number that fulfills those requirements."
    while True:
        number += 1
        if is_featured(number):
            return number
    
    
print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True
