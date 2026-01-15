import turtle
import random

wn = turtle.Screen()
wn.setup(900, 900)
wn.bgcolor('white')

player = turtle.Turtle()
player.shape('turtle')
player.color('black')
player.speed(2)

for i in range(5):
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)

    player.penup()
    player.goto(x, y)
    player.pendown()
    size = random.randint(10, 100)
    for i in range(3):
        player.forward(size)
        player.left(120)