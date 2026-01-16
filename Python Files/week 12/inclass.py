
'''
total = 0
user_input = input('enter a number of tupe done: ')

while user_input != 'done':
    user_number = float(user_input)
    total += user_number
    user_input = input('enter a number of yupe done: ')



from random import randint
my_file = open ('numbers.text', 'w')

for index in range(0,100):
    number = randint(50,250)
    my_file.write(str(number)+'\n')

other_file = open('numbers.txt', 'r')


my_file.close()


my_file = open('number.text', 'r')

data = my_file.read()
print(data)
for element in data:
    print(element)


class object:
    def __init__(self,x,y):
        self.x = x 
        self.y = y
        



'''

class playlist:
    def __init__(self, name = 'New playlist' , songs = []):
        self.name = name
        self.songs = songs 
        
    def add_song(self, song):
        self.songs.append(song)

    def __add__(self,other):
        combined = self.songs + other.name
        combined = self.songs + other.songs
        return playlist(combined_name, combined_songs)
    
    def __str__(self):
        return f'{self.name}{self.songs}'



p1 = playlist('x',['Song A', 'Song B'])

p2 = playlist('y',['Song C'])

combined = p1 + p2
print(combined)


class shoppingCart:
    def __intit__(self, items = {}):
        self.items = items
    
    def add_item(self, item):
        if item in self.items:
            self.items[item] +=1 
        else:
            self.items[item] = 1
    def __str__(self):
        return f'{self.items}'


p1 = shoppingCart({'tea':1, 'energy drink':2})
p1.add_item('clock')

print(p1)
p2 = shoppingCart({"energy drink :3, 'hat": 1})




class complexNumbers:
    def __init__(self, a , b):
        self.a = a 
        self.b = b
    def eq(self, other):
        return self.a == other.a and self.b == other.b
    def __str__(self):
        sign = '+' if self.b >= 0 else '-'
        return f'{self.a} {sign} {abs(self.b)}i'
    

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def mul(self, n):
        self.width*= n 
        self.height*= n

    def __mul__(self,n):
        return rectangle(self.width * n, self.height * n)
    
    def __str__(self):
        