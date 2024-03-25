'''
Author:Adam Cohill
Date Written: mm/dd/yy
Assignment : Module# exercise# part#
Description:

'''
strOutput1 = "purple"
strOutput2 = "orange"
strOutput3 = "green"
strColor1 = "red"
strColor2 = "yellow"
strColor3 = "blue"
boolValid = True
userInput1 = "Not set yet"
userInput2 = "Not set yet"
PROMPT = "Enter a primary color, DO NOT repeat colors.(red, yellow, blue)"
EXT_MSG = "The program will exit."

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

def inputValidation():
    global boolValid, userInput1, strColor1, strColor2, strColor3

    strInput = "not set yet"

    try:
        strInput = str(userInput1)
    except:
        print("Your input is not a primary color.")
        oneBlankLine()
        print(EXT_MSG)
        boolValid = False
    else:
        userInput2 = str(strInput)
        if strInput != userInput2:
            print("Your input value is not a string.")
            print(EXT_MSG)
            oneBlankLine()
            boolValid = False
        else:
            if strInput not in [strColor1, strColor2, strColor3]:
                print("Your input is not a primary color.")
                print(EXT_MSG)
                oneBlankLine()
                boolValid = False
            else:
                boolValid = True

def inputData1():
    global strColor1, strColor2, strColor3
    global userInput1, userInput2, boolValid

    userInput1 = input("Enter a color: ")
    print("The color you entered is:", userInput1)
    inputValidation()
    strColor1 = userInput1
    if userInput1 == strColor2:
        strColor2 = userInput1
    elif userInput1 == strColor3:
        strColor3 = userInput1
            

def inputData2():
    global strColor1, strColor2, strColor3
    global userInput1, userInput2, boolValid
    userInput2 = input("Enter a color: ")
    print("The color you entered is:", userInput2)
    inputValidation()
    strColor1 = userInput2
    if userInput1 == strColor2:
        strColor2 = userInput2
    elif userInput1 == strColor3:
        strColor3 = userInput2

def outputData():
    if userInput1 == strColor1 and userInput2 == strColor2:
        print(userInput1," and ",userInput2," makes ",strOutput2)
    elif userInput1 == strColor1 and userInput2 == strColor3:
        print(userInput1," and ",userInput2," makes ",strOutput1)
    else:
        print(userInput1," and ",userInput2," makes ",strOutput3)
    


inputData1()
inputData2()
outputData()
endOfProgram()
                
