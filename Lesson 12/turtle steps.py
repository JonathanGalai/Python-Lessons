import turtle
import random

wn = turtle.Screen()
wn.setup(900, 900)
wn.bgcolor('white')

player = turtle.Turtle()
player.shape('turtle')
player.color('black')
player.speed(2)

total_steps = 0

while total_steps < 500:
    steps = random.randint(1, 50)
    angle = random.randint(0, 360)  # כיוון אקראי
    player.left(angle)
    player.forward(steps)
    total_steps += steps

turtle.done()
