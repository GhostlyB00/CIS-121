#Seth Johnson

#1324
#62
#331
#4
'''
larger_num= int(input('enter a large number: '))
smaller_num= int(input('enter a small number: '))

num = 0
while larger_num > smaller_num:
    larger_num /= 2 
    num += 1

print(f"Number of times havled: {num} ")

#question 2
#counterattack

#o n e a t c

word = input ("enter a word: ")
result = ''
# first starting point, Ending point, step size
for i in range(1  , len(word) - 1,2):
    result += word[i]

print(f"output = {result}")



#question 3 
for number in range(0,11,2):
    print(number)


#question 4
word = '' 
while True:
    user_input = input('enter a letter: ')
    if user_input =='done':
        break
    else:
        word += user_input
print(f'the final word is {word}')

'''

#question 5
sum = 0
for number in range(51, 517, 2):
    sum += number
print(sum)