def append_to_list(value, lst=None):
    lst = lst or []
    lst.append(value)
    return lst


print(append_to_list(1) == [1])
print(append_to_list(2) == [2])

print(append_to_list(2))
print(append_to_list(3))
