'''
Author:Adam Cohill
Date Written: 06/15/23
Assignment : Module2 programming assignment pt.2
Description: Write a program that lets the user enter a nonnegative integer then uses a loop
to calculate the factorial of that number. Display the factorial.

'''

def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Get user input
num = int(input("Enter a nonnegative integer: "))

# Check if the number is nonnegative
if num < 0:
    print("Invalid input. The number must be nonnegative.")
else:
    result = calculate_factorial(num)
    print("Factorial of", num, "is", result)
