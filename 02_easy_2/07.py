# def multiply_list(lst1, lst2):
#     products = []
#     for idx in range(len(lst1)):
#         products.append(lst1[idx] * lst2[idx])
#     return products


def multiply_list(numbers1, numbers2):
    return [a * b for a, b in zip(numbers1, numbers2)]


list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True
