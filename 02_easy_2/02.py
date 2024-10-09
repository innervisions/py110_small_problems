def union(list1, list2):
    union = set()
    for el in list1:
        union.add(el)
    for el in list2:
        union.add(el)
    return union

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True
