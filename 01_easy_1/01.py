numbers = []

numbers.append(input('Enter the 1st number: '))
numbers.append(input('Enter the 2nd number: '))
numbers.append(input('Enter the 3rd number: '))
numbers.append(input('Enter the 4th number: '))
numbers.append(input('Enter the 5th number: '))
numbers.append(input('Enter the last number: '))

if numbers[-1] in numbers[:-1]:
    print(f'{numbers[-1]} is in {','.join(numbers[:-1])}.')
else:
    print(f'{numbers[-1]} is not in {','.join(numbers[:-1])}.')
