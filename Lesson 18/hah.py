import turtle
import random

onclick_player = turtle.Turtle()
onclick_player.shape("turtle")
onclick_player.color("white")
onclick_player.pu()

win = turtle.Screen()
win.bgcolor("black")
win.setup(width=800, height=600)

turtlesize = random.randit(1 - 5)


def move_turtle(x, y):
    onclick_player.goto(x, y)
    onclick_player.write(x, y)

def turtle_size():
    onclick_player.size(turtlesize)

win.onclick(move_turtle)
onclick_player.onclick(turtle_size)
turtle.mainloop()