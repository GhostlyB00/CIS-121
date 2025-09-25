#Seth Johnson
#functions

#write a function that adds 2 and multiply by 4 prints the results
import math
def my_function(number):
    number +=2 
    number *=4
    return number
def add_ten(number):
    number + 10
    return number


#starting with value 10, add 2, then multiply by 4. take the results and add two to it, then muitply by 4 again
result1 = add_ten(my_function(10))
result2 = my_function(result1)
my_function(200)

#call the function my_function 100 times

result = 10 
for number in range (0,10):
    result = my_function(result)
print(result)



#write a function that returns a product that return the product of two arguments
def product(num1 , num2):
    product = num1 * num2
    return product

print(product(4,3))
print(4*3)