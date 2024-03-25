'''
Author:Adam Cohill
Date Written: 06/07/23
Assignment : Module1 Meal Assignment
Description: a program that calculates the total
amount of a meal purchased at a restaurant.
The program should ask the user to enter the charge for the food,
then calculate the amounts of a 18 percent tip and 7 percent sales tax.

'''
mealAmount = 999.999
totalAmount = 999.999
tipAmount = 999.999
salesTaxAmount = 999.999
userInput = "not set yet"

def oneBlankLine():
    print(" ")

def twoBlankLines():
    print(" ")
    print(" ")

def welcomeMessage():
    twoBlankLines()
    print(__doc__)
    twoBlankLines()
    
def endOfProgram():
    twoBlankLines()
    print("End Of Program")
    twoBlankLines()
    
def inputData():

    global mealAmount , userInput

    PROMPT1 = "Enter the cost of your meal: $"

    userInput = input(PROMPT1)

    mealAmount = float(userInput)

def outputData ():
    twoBlankLines()
    print ("An 18 percent tip for this amount is: $", "%.2f" % tipAmount)
    print ("Sales tax for this amount is: $", "%.2f" % salesTaxAmount)
    print ("The total price of your meal is: $", "%.2f" % totalAmount )

welcomeMessage()
inputData()

tipAmount = mealAmount * 0.18
salesTaxAmount = mealAmount * 0.07
totalAmount = mealAmount + salesTaxAmount + tipAmount

outputData()
endOfProgram()

