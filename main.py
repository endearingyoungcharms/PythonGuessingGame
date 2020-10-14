from random import randint

global lives
lives = 5

global humanguess

number = randint(1,100)

def ask():
    humanguess = int(input('I am thinking of a number from 1 to 100. What is it? '))
    if humanguess > 100 or humanguess < 1 :
        print ('Please enter a number from 1 to 100')
        ask()
    else:
        check(number,humanguess,lives)
    

def check(number,humanguess,lives):
    if lives > 0:
        if number == humanguess:
            print('You guessed correctly!')
        elif number>humanguess:
            print('Oops! Too low!')
            lives = lives - 1
            print(lives)
            ask()
        else:
            print ('Way too high!')
            lives = lives - 1
            print (lives)
            ask()
    else:
        print("Game Over.")
    
if __name__ == '__main__':
    ask()