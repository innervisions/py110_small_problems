# def swap_name(name):
#     first_name, last_name = name.split()
#     return f'{last_name}, {first_name}'


def swap_name(name):
    names = name.split()
    return f'{names[-1]}, {' '.join(names[:-1])}'


print(swap_name('Joe Roberts') == "Roberts, Joe")   # True
print(
    swap_name("Karl Oskar Henriksson Ragvals") == "Ragvals, Karl Oskar Henriksson"
)  # True
