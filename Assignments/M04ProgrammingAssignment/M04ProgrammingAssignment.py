'''
Author:Adam Cohill
Date Written: 07/02/23
Assignment :  A positive integer greater than 1
is said to be prime if it has no divisors other than 1 and itself.
A positive integer greater than 1 is composite if it is not prime.
Write a program that asks the user to enter an integer greater than 1,
then displays all of the prime numbers
that are less than or equal to the number entered

'''


num = int(input("Enter a number greater than 1, I will show you all primenumbers betweenyournumberand 1: "))

# Create an empty list to store prime numbers
prime_numbers = []

# Iterate from num down to 2 (inclusive)
for i in range(num, 1, -1):
    is_prime = True

    # Iterate from 2 to the square root of i (inclusive)
    for j in range(2, int(i ** 0.5) + 1):
        # Check if i is divisible evenly by j
        if i % j == 0:
            is_prime = False
            break

    # If is_prime is still True, i is a prime number, so add it to the list
    if is_prime:
        prime_numbers.append(i)

# Print the list of prime numbers
print("Prime numbers between", num, "and 1:", prime_numbers)
