

'''
for number in range(0,11,2):
    print(number)

for number in range (1,11):
    if number % 2 == 0:
        print(number)


user_number = int(input('please enter a number: '))
for number in range (5 ,user_number +1 ):
    if number % 2 ==1:
        print(number) 
'''

total = 0 
for number in range (0,50):
    user_number = input('enter number a number: ')
    if user_number =='q':
        break
    total += int(user_number)