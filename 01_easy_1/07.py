def swap_word(word):
    if len(word) < 2:
        return word
    return word[-1] + word[1:-1] + word[0]

def swap(text:str) -> str:
    words = text.split()
    swapped_words = [swap_word(word) for word in words]
    return ' '.join(swapped_words)


print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True
