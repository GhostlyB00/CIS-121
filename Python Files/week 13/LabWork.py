
'''

import random


with open('QuizInts.txt', 'w') as txt_file:
    for i in range(100):
        num = random.randint(50,100)
        txt_file.write(str(num) + "\n")





'''

# question  7
total_vistor = 0 
num_of_days = 0


with open("Python Files/week 13/LibraryVisits.csv","r") as lib_visits:
    for _row in lib_visits:
        print(_row)

    values = _row.split(',')
    total_vistor += int(values[1])
    num_of_days += 1

print(f'Average Visitors over {num_of_days} days is {total_vistor / num_of_days}')