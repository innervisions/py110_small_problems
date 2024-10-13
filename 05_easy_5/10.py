def unique_sequence(numbers):
    return [
        value
        for idx, value in enumerate(numbers)
        if idx == 0 or value != numbers[idx - 1]
    ]


original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)  # True
