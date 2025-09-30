# worked on by Seth Johnson
def pramind_volume(base, height):
    volume= (b**2 * height) / 3
    return volume

print(f'The volume of the pyramid is {pramind_volume(3,4)}')


#Question 8
def pool_times(grade,time):
    #complete this
    pool_times = ''
    if grade == 'k':
        grade = 0
    
    # checks grade is k or between 1-3 
    if 0 <= int(grade) <=3:
        if(time == 'morning'):
            pool_times = '9 AM'
        else:
            pool_times = '1 PM'

    elif (4 <= int(grade)<= 8):
        if(time == "morning"):
            pool_times = "11 AM"
        else:
            pool_times = "3 PM"
    
    return pool_times

print(f' Pool time is : {pool_times('K', 'morning')}')


#question 11
#knuts , sickles , galleons
#1 galleon == 493 knuts
#1 sickle = 29 nuts

def convert_knuts(knuts):


    galleons = knuts // (493)
    remaining_knuts = knuts - (galleons * (493))

    sickles = remaining_knuts // 29

    remaining_knuts = remaining_knuts - (sickles * 29)

    output  = ''

    if knuts > 0 :
        output += f'knuts  : {galleons}'
    if sickles > 0:
        output += f"sickles : {sickles}"
    if galleons > 0:
        output += f"galleons : {remaining_knuts}"

        return output
    
print(convert_knuts(32))    



#question 14

from random import randint

def guess_num(user_guess):
    output = ''
    value = randint(0,9)

    if user_guess == "even":
        if value % 2 ==0:







# question 1 for strings

def is_fever(input):
    if is_fever 'f':
    