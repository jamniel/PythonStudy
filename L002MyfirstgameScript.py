import random
secret = random.randint(1,10)
print('-------Guess my number----------')
temp=input("Please guess the number I\'m think of now:")
guess=int(temp)
while guess != secret:
    temp=input("Oops, you are wrong, please guess again:")
    guess=int(temp)
    if guess == secret:
        print("Bravo, you are right!")
    else:
        if guess > secret:
            print('Your number is too big.')
        else:
            print('Your number is too small')
print("Game Over")
