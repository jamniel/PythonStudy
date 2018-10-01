import random
secret = random.randint(1,10)
print('-------Guess my number----------')
i=3
guess = 0
print ("Please guess the number I\'m think of now:", end=" ")
while guess != secret and i > 0:
    temp=input()
    if temp.isdigit():
        guess=int(temp)
        i=i-1
        if guess == secret:
            print("Bravo, you are right!")
        else:
            if guess > secret:
                print('Your number is too big.')
            else:
                print('Your number is too small')
            if i > 0:
                print('try again:', end='')
            else:
                print('Sorry, you have no more chance.')
    else:            
        i=i-1
        if i > 0:
            print('Your input is invalid, please enter a number:', end='')
        else:
            print('Sorry, you have no more chance.')
print("Game Over")
