def letter_counter(a_string):
    letter_count = {}
    for letter in a_string:
        letter_count[letter] = a_string.count(letter)
    return letter_count
  
def word_histogram(a_string):
    word_count = {}
    this_thing = a_string.lower().split()
    for word in this_thing:
        word_count[word] = this_thing.count(word)
    return word_count and this_thing
def histogram_rank(a_string):
    word_count = {}
    this_thing = a_string.lower().split()
    for word in this_thing:
        word_count[word] = this_thing.count(word)
    word_count_sorted = sorted(word_count.items(), key=lambda x: x[1])
    print(f'The top three words are:\n{word_count_sorted[-1]}\n{word_count_sorted[-2]}\n{word_count_sorted[-3]}')
        

print(letter_counter("Bananas"))
print(word_histogram("To be or not to be"))
histogram_rank("to be or not to be or to be or maybe even to not to be lol")
