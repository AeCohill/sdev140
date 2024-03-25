import turtle, random

myPen = turtle.Turtle()
turtle.Screen().bgcolor("#3fa652")
myPen.shape("arrow")
myPen.pensize(2)
myPen.speed(10)
myPen.color("white")
myPen.write("Turtle Race!", align='center',  font=("Arial", 20, "normal"))
#Start Line
myPen.penup()
myPen.goto(-160, 150)
myPen.pendown() 
myPen.goto(-160, 0)
#Turtles
#Let's add our turtles
redTurtle = turtle.Turtle()
redTurtle.shape('turtle')
redTurtle.color('red')
redTurtle.pensize(2)
redTurtle.penup()
redTurtle.goto(-180, 140)
redTurtle.pendown()

greenTurtle = turtle.Turtle()
greenTurtle.shape('turtle')
greenTurtle.color('green')
greenTurtle.pensize(2)
greenTurtle.penup()
greenTurtle.goto(-180, 110)
greenTurtle.pendown()

blueTurtle = turtle.Turtle()
blueTurtle.shape('turtle')  
blueTurtle.color('blue')
blueTurtle.pensize(2)
blueTurtle.penup()
blueTurtle.goto(-180, 80)
blueTurtle.pendown()

yellowTurtle = turtle.Turtle()
yellowTurtle.shape('turtle')
yellowTurtle.color('orange')
yellowTurtle.pensize(2)
yellowTurtle.penup()
yellowTurtle.goto(-180, 50)
yellowTurtle.pendown()

#Let's start the race!
while True:
  redTurtle.forward(random.randint(1,8))
  greenTurtle.forward(random.randint(1,8))
  blueTurtle.forward(random.randint(1,8))
  yellowTurtle.forward(random.randint(1,8))
  
  if redTurtle.xcor()>180:
    print("Red Turtle wins!")
    break
  elif greenTurtle.xcor()>180:
    print("Green Turtle wins!")
    break
  elif blueTurtle.xcor()>180:
    print("Blue Turtle wins!")
    break
  elif yellowTurtle.xcor()>180:
    print("Yellow Turtle wins!")
    break
