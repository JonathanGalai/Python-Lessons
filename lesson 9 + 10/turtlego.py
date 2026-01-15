import turtle
import time

sc = turtle.Screen()
sc.setup(1200,900)
sc.bgcolor('cyan')

player = turtle.Turtle()
player.shape('turtle')
player.color('red')
player.pensize(2)
player.penup()
player.speed(10)

def go_right():
    player.setheading(0)
    player.forward(10)

def go_left():
    player.setheading(180)
    player.forward(10)

def go_up():
    player.setheading(90)
    player.forward(10)

def go_down():
    player.setheading(270)
    player.forward(10)

turtle.listen()
turtle.onkey(go_right,'Right')
turtle.onkey(go_left,'Left')
turtle.onkey(go_up,'Up')
turtle.onkey(go_down,'Down')

ball = turtle.Turtle()
ball.shape('circle')
ball.penup()
ball.speed(1)

# SLOW movement
move_ver = 1
move_hor = 2

playersize = 1
player.shapesize(playersize)

while True:
    ball.setpos(ball.xcor() + move_hor, ball.ycor() + move_ver)

    if ball.xcor() > 350 or ball.xcor() < -350:
        move_hor *= -1

    if ball.ycor() > 350 or ball.ycor() < -350:
        move_ver *= -1

    if player.distance(ball) <= 20:
        playersize += 0.5
        player.shapesize(playersize)

    time.sleep(0.01)   # slow animation

turtle.mainloop()
