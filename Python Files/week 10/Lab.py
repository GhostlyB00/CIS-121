class Product:
    name = ""
    price = ''

        
    def __init__(self, input_name, input_price):
        self.name = input_name
        self.price = input_price
        self.quantity = 0

    def get_price(self):
        return self.price
    
    def set_price(self, value):
        if self.price > 0:
            self.price = value


    def __str__(self):
        return f"The Product is {self.name} and priced at {self.price} we have {self.quantity}"
    
    @property
    def quantity(self, value):
        if 0 <= value <99:
            self.quantity = value
       
    
appleiphone17ProMax = Product("Iphone 17 Pro Max", 1499)
appleiphone17pro = Product("Iphone 17 Pro", 1000)
appleiphone17 = Product("Iphone 17", 990)

print(appleiphone17ProMax)
print(appleiphone17pro)
print(appleiphone17)

appleiphone17.quantity = 2

class Books:
    name = ''
    price = ''

    def __init__(self, title, author, page_count ):
        self.title = title
        self.author = author
        self.page_count = page_count
    
    
    #get price
    def get_price(self):
        if self.price > 0:



    #setter
    def set_price(self):
        self.qauntity = ''



class Student:
    def __init__(self):
        self.name = "Unknown"
        self.name = "Unknown"
        self.gpa = 0

    def get_names(self):
        return self.name
    def set_name(self, value):
        self.name = value
    
    def get_major(self):
        return self.major 
    def set_major(self, value):
        self.major = value

    def get_gpa(self):
        return self.gpa
    def set_gpa(self, value):
        if 0 <= value <=4.0:
            self.gpa = value
    
    def introduce(self):
        return f"Hi, Im {self.name}. Im studying {self.major}"
    
    def study_for_exam(self):
        if self.gpa < 4.0:
            self.gpa += 0.2

student1 = Student()
student1.set_name = "Evan Linder"
student1.set_major = "computer science"
student1.set_gpa = 3.8
student1.study_for_examp()


print(student1>introduce())
print(student1.get_gpa())
