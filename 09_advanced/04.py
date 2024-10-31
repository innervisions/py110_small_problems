# def merge(lst1, lst2):
#     idx1 = 0
#     idx2 = 0
#     result = []
#     while idx1 < len(lst1) or idx2 < len(lst2):
#         if idx1 >= len(lst1):
#             result.append(lst2[idx2])
#             idx2 += 1
#         elif idx2 >= len(lst2):
#             result.append(lst1[idx1])
#             idx1 += 1
#         elif lst1[idx1] < lst2[idx2]:
#             result.append(lst1[idx1])
#             idx1 += 1
#         else:
#             result.append(lst2[idx2])
#             idx2 += 1
#     return result


def merge(list1, list2):
    copy1 = list1[:]
    copy2 = list2[:]
    result = []

    while copy1 and copy2:
        if copy1[0] <= copy2[0]:
            result.append(copy1.pop(0))
        else:
            result.append(copy2.pop(0))

    return result + copy1 + copy2


# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)
