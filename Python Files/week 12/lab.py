# question 5

class RGBColor:
   # for each parameter is ranges from (0 - 255)
    def __init__(self,r,g,b):
        self.r = r
        self.g = g 
        self.b = b

    def __add__(self, color2):
        color3 = RGBColor(0,0,0)
        color3.r = (self.r + color2.r) / 2
        color3.g = (self.g + color2.g) / 2
        color3.b = (self.b + color2.b) / 2

    def __str__(self):
        return f"RGB Values: ({self.r}), {self.g}, {self.b}"
    
c1= RGBColor(170, 150, 200)
c2 = RGBColor(30, 100, 60)
c3 = c1 +c2
print ('color 1 = ' , c1)
print ('color 1 - ' , c2)
print ('color 1 - ' , c3)


# quesiton 1

class Vector:
    def __init__(self, x , y):
        self.a = x 
        self.b = y
    
    def __eq__(self, vector2):
        self.a == vector2.a and self.b == vector2.b

    def __str__(self):
        return f'vector: ({self.a}, {self.b})'
    
Vector1= Vector(3,4)
Vector2 = Vector(1,4)
print('Is vector 1 and 2 same ?')
print(Vector == Vector2)


# question 2
class point:
    def __init__(self, x, y):
        self. 

   


