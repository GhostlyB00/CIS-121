class Dog:
    def __init__(self,_breed,_color,_size):
        self.breed = _breed
        self.color = _color
        self.color = _size

    def get_breed(self):
        return self.breed
    
    def get_color(self):
        return self.color
    
    def get_size(self):
        return self.size
    def speak(self):
        print('Bark')
    
class dogPark:
    def __init__(self, _name):
        self.name = _name
        self.dogs = []
    def add_dog(self, dog):
        self.dogs.append(dog)
    def show_dogs(self):
        for dog in self.dogs:
            print(dog.get_name())
    def change_dog_name(self, old_name, new_name):
        for dog in self.dogs:
            if dog.get_name() == old_name:
                dog.set_name(new_name)
    def find_dog(self, dog_name):
        for dog in self.dogs:
            if dog.get_name() == dog_name:
                dog.speak()




            
park1 = DogPark('Bark Zone')

park1.add_dog(Dog('spot', 2, 'lab'))
park1.add_dog(Dog("Rover", 3 , 'mastiff'))

park1.show_dogs()
park1.change_dog_name("spoot", "spot")
park1.show_dogs()

park1.find_dog("Rover")