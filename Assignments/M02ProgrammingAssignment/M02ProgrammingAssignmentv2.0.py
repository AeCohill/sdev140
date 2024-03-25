'''
Author:Adam Cohill
Date Written: 06/15/23
Assignment : Module2 programming assignment pt.2
Description: Write a program that takes in 2 primary
colors and outputs the corisponding
secondary color

'''

def inputValidation(color):
    if color not in ["red", "blue", "yellow"]:
        print("Your input is not a primary color.")
        return False
    return True

def userInputs():
    primaryColor1 = input("Enter First Primary Color: ")
    while not inputValidation(primaryColor1):
        primaryColor1 = input("Enter First Primary Color: ")

    primaryColor2 = input("Enter Second Primary Color: ")
    while not inputValidation(primaryColor2):
        primaryColor2 = input("Enter Second Primary Color: ")
        
    if ((primaryColor1 == "red" and primaryColor2 == "blue") or (primaryColor1 == "blue" and primaryColor2 == "red")):
        secondaryColor = "purple"

    if ((primaryColor1 == "red" and primaryColor2 == "yellow") or (primaryColor1 == "yellow" and primaryColor2 == "red")):
        secondaryColor = "orange"

    if ((primaryColor1 == "blue" and primaryColor2 == "yellow") or (primaryColor1 == "yellow" and primaryColor2 == "blue")):
        secondaryColor = "green"

    print(primaryColor1, "and", primaryColor2, "make", secondaryColor)

userInputs()
