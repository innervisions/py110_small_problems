def triangle(a, b, c):
    angles = [a, b, c]
    if sum(angles) != 180 or any(angle <= 0 for angle in angles):
        return 'invalid'
    if any(angle == 90 for angle in angles):
        return 'right'
    if any(angle > 90 for angle in angles):
        return 'obtuse'
    return 'acute'


print(triangle(60, 70, 50) == "acute")  # True
print(triangle(30, 90, 60) == "right")  # True
print(triangle(120, 50, 10) == "obtuse")  # True
print(triangle(0, 90, 90) == "invalid")  # True
print(triangle(50, 50, 50) == "invalid")  # True
