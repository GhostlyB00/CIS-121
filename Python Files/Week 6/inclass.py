'''
lyst = ['Monday', 'tuesday', 'wednesday', 'thursday', 'friday']

#print (x[2])
#print(x[1:4])
#for element in lyst:
#   print(element)



print(lyst)
lyst.append('saturday')
lyst.append('sunday')
print(lyst)


word = 'apple'
word += 'e'
print(word)


print(lyst[2][3:6])



x = 'Wednesday'
print(x[3:6])


print(lyst[4])

lyst[4] = 'Funday'

print(lyst)



word = 'apfel'
print(word)


word[2] = 'p'
print(word[2])


x = 'apple'
y = x

print(x)
print(y)

x += 's'
print(x)
print(y)

#muteable object

x = ['Monday', 'tuesday', 'wednesday', 'thursday', 'friday']
y = x 

print(x)
print(y)

x[4] = 'funday'

print(x)
print(y)


workdays = (['Monday', 'tuesday', 'wednesday', 'thursday', 'friday'])
print(workdays)
workdays[4]
print(workdays)
'''

#write a function that takes a string as a arugment and returns a lyst containing all of the words in that string
word = 'Peter Piper picked a peck of pickled peppers.'
result = ['Peter', 'piper', 'picked', 'a', 'peck', 'of', 'picked', 'peppers.']

def string_to_list(word):
    words = []
    #collect a word
    built_word = ''
    for letter in word:
        if letter == ' ':
            words.append(built_word)
            built_word = ''
        else:
            built_word += letter
        
        return words
print(string_to_list(word))
