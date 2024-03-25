'''
Author:Adam Cohill
Date Written: 06/07/23
Assignment : M01 Programming Assignment
Description: Write a program that converts Celsius
temperatures to Fahrenheit temperatures.

'''

calculation = 999.999
userInput = 999.999
strInput = "not set yet"

def blankLine ():
    print (" ")

def inputData():
    global strInput, userInput

    PROMPT1 = "Enter a tempature between 1.0 and 999.0 in Celsius to convert to Fahrenheit: "

    strInput = input(PROMPT1)

    userInput = float(strInput)

def outputData ():
    blankLine()
    print(strInput, " degrees Celsius is ", calculation, " degrees Fahrenheit.")

def endProgram ():
    blankLine()
    print ("End Of Program")


inputData()

calculation = 9 / 5 * userInput +32

outputData()
endProgram()
