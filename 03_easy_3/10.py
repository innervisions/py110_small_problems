def is_balanced(string):
    left = 0
    right = 0
    for char in string:
        if char == '(':
            left += 1
        if char == ')':
            right += 1
        if right > left:
            return False
    if left != right:
        return False
    return True
    
    
print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True
