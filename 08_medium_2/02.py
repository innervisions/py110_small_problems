def triangle(a, b, c):
    sides = sorted([a, b, c])
    if any(side <= 0 for side in sides) or sides[0] + sides[1] <= sides[2]:
        return 'invalid'
    if sides[0] == sides[1] == sides[2]:
        return 'equilateral'
    if sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
        return 'isosceles'
    return 'scalene'

print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True
