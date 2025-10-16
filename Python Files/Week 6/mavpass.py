word = 'Aeiou'
reverse_string = ''
for i in range (len (word) - 1, -1, -1):
    reverse_string += word[i]
print(reverse_string)

#this is another way to do it
def reverse_string(word):
    reversed_word = ''
    for char in word:
        reversed_word = char + reversed_word
    return reversed_word


