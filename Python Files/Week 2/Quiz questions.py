import math

#1
a = float(input('enter a: '))
b = float(input('enter b: '))
h = float(input('enter h: '))




area = ((a+b)/2)*h

print(f'area is {area}')

#2
r= int(input('please enter r value: '))
h= int(input('please enter h value: '))

volume= math.pi * r**3 * h
print(f'volume is {volume}')




#3 did these in class
r = 10

volume = (4/3)*math.pi * (r**3)
print(f'volume is {volume}') 


#4

area= 2/3 * math.pi * r**2

a= input('Please enter A:')
r= input('Please enter R:')

print(f'area is {area}')

#5
b= input('please enter b: ')
h= input('please enter h: ')

volume= (b**2*h)/3
print(f'volume is {volume}') 

#6
r= input('please enter r: ')
h= input('please enter h: ')


v= math.pi * r**2*h/3
print(f'volume is {volume}') 

#7

a = input(int('please enter 3 pointers scored: '))
b = input(int('please enter 2 pointers scored: '))
#3a + 2b=r r=(3*a)+(2*b)
print ('you made 3 {a} pointers + 2 {b} pointers, your score would be' ({3}+{2}))



#8
chickens= int(input('please enter number of chickens: '))
cows= int(input('please enter number of cows: '))
pigs= int(input('please enter number of pigs: '))


total_legs= (2*chickens)+(4*cows)+(4*pigs)
print(f'total legs are {total_legs}')

