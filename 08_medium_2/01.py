def get_percent(value, total):
    percent = value / total * 100
    return f'{percent:.2f}'

def letter_percentages(string:str) -> dict:
    tally = {
        'lowercase': 0,
        'uppercase': 0,
        'neither': 0
    }
    for char in string:
        if char.islower():
            tally['lowercase'] += 1
        elif char.isupper():
            tally['uppercase'] += 1
        else:
            tally['neither'] += 1
    total = sum(tally.values())
    return {key: get_percent(value, total) for key, value in tally.items()}
    

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)
