def count_occurrences(lst):
    occurrences = {}
    for item in lst:
        occurrences[item] = occurrences.get(item, 0) + 1
    
    for key, value in occurrences.items():
        print(f'{key} ==> {value}')

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)
