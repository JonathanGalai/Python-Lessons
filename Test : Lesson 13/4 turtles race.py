import turtle
import random
import time

#screen
wn = turtle.Screen()
wn.setup(1000, 1000)
wn.bgcolor('white')

#player 1
turtle1 = turtle.Turtle()
turtle1.shape('turtle')
turtle1.color('black')
turtle1.speed(2)

#player 2
turtle2 = turtle.Turtle()
turtle2.shape('turtle')
turtle2.color('red')
turtle2.speed(2)

#player 3
turtle3 = turtle.Turtle()
turtle3.shape('turtle')
turtle3.color('green')
turtle3.speed(2)

#player 4
turtle4 = turtle.Turtle()
turtle4.shape('turtle')
turtle4.color('blue')
turtle4.speed(2)

#pen
pen = turtle.Turtle()
pen.shape('arrow')
pen.color('black')
pen.speed(2)

#message
message = turtle.Turtle()
message.hideturtle()
message.penup()
message.goto(0, 0)

#game

#turtle 2, 3, 4 go down
turtle1.penup()
turtle1.right(90)
turtle1.forward(50)
turtle1.left(90)
turtle2.penup()
turtle2.right(90)
turtle2.forward(150)
turtle2.left(90)

turtle3.penup()
turtle3.right(90)
turtle3.forward(250)
turtle3.left(90)

turtle4.penup()
turtle4.right(90)
turtle4.forward(350)
turtle4.left(90)

# line
pen.penup()
pen.goto(350, 350)
pen.right(90)
pen.pendown()
pen.forward(850)

while turtle1.xcor() <335 and turtle2.xcor() <335:
    #randoms
    distance1 = random.randint(1, 75)
    distance2 = random.randint(1, 75)
    distance3 = random.randint(1, 75)
    distance4 = random.randint(1, 75)



    #walk
    turtle1.forward(distance1)
    turtle2.forward(distance2)
    turtle3.forward(distance3)
    turtle4.forward(distance4)


    if turtle1.xcor() >= 345:
        message.penup()
        message.goto(0, 0)
        message.write("Player 1 Won!",font=("Arial", 28, "normal"))
        time.sleep(2)
        break
    if turtle2.xcor() >= 345:
        message.penup()
        message.goto(0, 0)
        message.write("Player 2 Won!",font=("Arial", 28, "normal"))
        time.sleep(2)
        break
    if turtle3.xcor() >= 345:
        message.penup()
        message.goto(0, 0)
        message.write("Player 3 Won!",font=("Arial", 28, "normal"))
        time.sleep(2)
        break
    if turtle4.xcor() >= 345:
        message.penup()
        message.goto(0, 0)
        message.write("Player 4 Won!",font=("Arial", 28, "normal"))
        time.sleep(2)
        break