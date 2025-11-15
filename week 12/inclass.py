
'''
total = 0
user_input = input('enter a number of tupe done: ')

while user_input != 'done':
    user_number = float(user_input)
    total += user_number
    user_input = input('enter a number of yupe done: ')

'''

from random import randint
my_file = open ('numbers.text', 'w')

for index in range(0,100):
    number = randint(50,250)
    my_file.write(str(number)+'\n')

other_file = open('numbers.txt', 'r')


my_file.close()



        