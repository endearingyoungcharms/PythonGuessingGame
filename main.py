from random import *
from time import sleep

number = randint(1,100)

def ask():
    humanguess = int(input('I am thinking of a number from 1 to 100. What is it? '))
    if humanguess > 100 or humanguess < 1 :
        print ('Please enter a number from 1 to 100')
    else:
        check(number,humanguess)
    

def check(number,humanguess):
    if number == humanguess:
        print('You guessed correctly!')
    elif number>humanguess:
        print('Oops! Too low!')
        ask()
    else:
        print ('Way too high!')
        ask()
    
if __name__ == '__main__':
    ask()