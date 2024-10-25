NUMBER_WORDS = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
                'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
# def word_to_digit(message):
#     
#     result = []
#     for word in message.split(' '):
#         if word.casefold() in NUMBER_WORDS:
#             result.append(NUMBER_WORDS[word.casefold()])
#         else:
#             result.append(word)
#     return ' '.join(result)

def word_to_digit(sentence):
    words = sentence.split()
    processed_words = [NUMBER_WORDS.get(word, word) for word in words]
    return " ".join(processed_words)


message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True
