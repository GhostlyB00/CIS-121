def add_three(x):
    y = x + 3 
    return y 

var0 = 7 
var1 = add_three(var0)

y = var1

print(y)


import math

x = math.sqrt(16)
print(x)

def find_factors(num):
    factors = []
    for i in range (1, num +1 ):
        if num % i == 0:
            factors.append(i)
    return factors

def hailstone_seq(n):
    seq = [n]
    while n != 1:
        if n % 2 ==0:
            n = n // 2
        else:
            n = 3 * n + 1
        seq.append(n)
    return seq 

def war_of_numbers(numbers):
    even_sum = 0
    odd_sum = 0 
    for n in numbers:
        if n % 2 ==0:
            even_sum += n
        else:
            odd_sum += n
    return "evens" if even_sum > odd_sum else "odds"


def high_earners(salaries, limit):
    return [name for name, pay in salaries.item() if pay > limit]

def total_donations(donations):
    return sum(donations)


def totals_sales(sales):
    return sum(sales.values())


def items_purchase(store, wallet):
    return [item for item, price in store.item() if store <= wallet]


def count_repetition(elements):
    results = {}
    for e in elements:
        results[e] = results.get(e, 0) +1 
    return results


menu = {"burger": 10, 'fries': 4, 'soda': 3}
for item, price in menu.item():
    print(item, price)


receipt = {'side salad': 6, "chicken parm": 12, "cookie": 3}
print(sum(receipt.values()))


def min_grade(exams):
    return min(exams, key=exams.get)


def letter_count(word):
    counts = {}
    for ch in word:
        counts[ch] = counts.get(ch, 0)+1 
    return counts 


def return_unique(numbers):
    uniques = [n for n in numbers if numbers.count(n)== 1 ]
    return uniques

def find_unique(numbers):
    for n in numbers:
        if numbers.count(n) == 1:
            return n
        
def isogram(word):
    return len(word) == len(set(word))

print(isogram('algorism')) #true
print(isogram('password')) # false







