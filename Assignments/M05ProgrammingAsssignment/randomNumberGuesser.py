'''
Author:Adam Cohill
Date Written: 06/15/23
Assignment : Write a function that generates a random number in the range of 1 through 100,
and asks the user to guess what the number is. If the user’s guess is higher than the random number,
the program should display “Too high, try again.” If the user’s guess is lower than the random number,
the program should display “Too low, try again.” If the user guesses the number,
the application should congratulate the user and generate a new random number so the game can start over 
'''
import random

num = random.randint(1, 100)
guess = None
firstGuess = True
#print(num) uncomment to cheat
while guess != num:
    if firstGuess:
        guess = input('Guess a number between 1 and 100: ')
        firstGuess = False
    else:
        if guess == str(num):
            print('YOU GUESSED CORRECTLY!!!!!')
            break
        elif int(guess) > num:
            guess = input("Your number is too high. Try again: ")
        elif int(guess) < num:
            guess = input("Your number is too low. Try again: ")
