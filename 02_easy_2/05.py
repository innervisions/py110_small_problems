# def interleave(lst1, lst2):
#     result = []
#     for idx in range(len(lst1)):
#         result.append(lst1[idx])
#         result.append(lst2[idx])
#     return result

import itertools

def interleave(lst1, lst2):
    return list(itertools.chain.from_iterable(zip(lst1, lst2)))

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True
