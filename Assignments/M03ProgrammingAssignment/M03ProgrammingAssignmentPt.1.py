'''
Author:Adam Cohill
Date Written: 06/25/23
Assignment : Module3 programming assignment pt.1
Description:Write a program that asks the user to enter a
series of single-digit numbers with nothing separating them.
The program should display the sum of all
the single-digit numbers in the string.



'''
userInput = input ("Enter a number, each integer in it will be added together: ")
digits = []

for digit in userInput:
    if digit.isdigit():
        digits.append(int(digit))
        
sumOfDigits = sum(digits)

print ("Sum of digits: ", sumOfDigits)
