def war_of_numbers(numbers):
    even_sum = 0 
    odd_sum = 0 
    for n in numbers:
        if n % 2 ==0:
            even_sum += n
        else:
            odd_sum += n
    return "evens" if even_sum > odd_sum else "odds"


def functions_of_numbers(numbers):
    even_sum = 0 
    odd_sum = 0 
    for n in numbers:
        if n % 2 == 0:
            even_sum += n
        else:
            odd_sum += n
    return "evens" if even_sum > odd_sum else "odds"