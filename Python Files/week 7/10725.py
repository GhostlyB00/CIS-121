#d = {'p': 9, 'e':???}
     
def letter_counter(word):
    letter_dictionary = {}
    if letter in word:
        if letter in letter_dictionary:
            letter_dictionary[letter] = letter_dictionary[letter] + 1
        else: 
            letter_dictionary[letter] = 1
    return letter_dictionary

my_word = 'peter piper picked a peck of pickled perpper'
print(letter_counter(my_word))

for letter in letter_dict:
    print(letter, letter_dict[letter])
