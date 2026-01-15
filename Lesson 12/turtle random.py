import turtle
import random

wn = turtle.Screen()
wn.setup(900, 900)
wn.bgcolor('white')

player = turtle.Turtle()
player.shape('turtle')
player.color('black')
player.speed(2)

min_angle = int(wn.textinput("Angle Setup", "Enter min angle:"))
max_angle = int(wn.textinput("Angle Setup", "Enter max angle:"))
min_distance = int(wn.textinput("Distance Setup", "Enter min distance:"))
max_distance = int(wn.textinput("Distance Setup", "Enter max distance:"))
min_pensize = int(wn.textinput("Pensize Setup", "Enter min pensize:"))
max_pensize = int(wn.textinput("Pensize Setup", "Enter min pensize:"))

while True:
    angle = random.randint(min_angle, max_angle)
    distance = random.randint(min_distance, max_distance)
    pensize = random.randint(min_pensize, max_pensize)

    player.pensize(pensize)
    player.left(angle)
    player.forward(distance)