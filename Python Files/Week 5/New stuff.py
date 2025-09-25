#write code to determine how many letters are in a word
# vowel = aieouy
#word = "hello world"
#word2 = 'apple and bananas'
#word3 = 'happy time'

def vowel_counter(passed_word):
    count = 0
    for letter in passed_word:
        if letter == 'a':
            count += 1
        elif letter == 'e':
            count += 1
        elif letter == 'i':
            count += 1
        elif letter == 'o':
            count += 1
        elif letter == 'u':
            count += 1
        elif letter == 'y':
            count += 1
    print(f'the vowel count in ' {passed_word}' is "{count})

word1 = "hello world"
word2 = 'apple and bananas'
word3 = 'happy time'

vowel_counter("hello world")
vowel_counter('apple and bananas')
vowel_counter('happy time')




































'''
word = "hello world"
word2 = 'apple and bananas'
word3 = 'happy time'
count = 0

word= 'hello world'
for vowel in word:
    if vowel == "a" or vowel == "e" or vowel == "i" or vowel == "o" or vowel == "u" or vowel 'y':
        count+=1
print(count)

word= 'hello apple and bananas'
for vowel in word:
    if vowel == "a" or vowel == "e" or vowel == "i" or vowel == "o" or vowel == "u" or vowel 'y':
        count+=1
print(count)




for letter in word:
    if letter =='a':
        count += 1
    if letter =='e':
        count += 1
    if letter =='i':
        count += 1
    if letter =='o':
        count += 1
    if letter =='u':
        count += 1
    if letter == 'y'
        count += 1
print(f'The vowel count in ',{word}, 'is', {count})
print(f'The vowel count in ',{word2}, 'is', {count2})
print(f'The vowel count in ',{word3}, 'is', {count3})
'''


''''
for letter in word:
    if letter !='':
        count+=1
print(count)
'''
