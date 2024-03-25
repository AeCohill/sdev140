'''
Author:Adam Cohill
Date Written: 06/25/23
Assignment : Module3 programming assignment pt.2
Write a program that writes a series of
random numbers to a file and displays allthe numbers to the console.
Each random number should be in the range of 1 through 500.
The application should let the user specify
how many random numbers the file will hold. 



'''

fileName = "Write_File.txt"
import random 

with open(fileName,'w')as file:
    userInput = input("Enter how many random numbers to generate: ")
    count = int(userInput)

    for _ in range(count):
        randomNumbers = random.randint(1,500)
        file.write(str(randomNumbers)+ '\n')
        print (randomNumbers)
