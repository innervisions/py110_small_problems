# def halvsies(lst: list) -> list:
#     length = len(lst)
#     if length % 2:
#         cutoff = (length // 2) + 1
#     else:
#         cutoff = length // 2

#     return [lst[:cutoff], lst[cutoff:]]


def halvsies(lst):
    half = (len(lst) + 1) // 2
    first_half = lst[:half]
    second_half = lst[half:]
    return [first_half, second_half]


# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])
