def sort_words_alphabetically(input_string):
    words = input_string.split()
    sorted_words = sorted(words)
    result_string = ' '.join(sorted_words)
    return result_string
input_string = "banana apple orange grape"
result = sort_words_alphabetically(input_string)
print(result)
