import turtle
import time

win = turtle.Screen()
win.setup(width=1200, height=700)
win.bgcolor("black")
win.title("2 Player Pong")
win.tracer(0)

player = turtle.Turtle()
player.color("white")
player.shape("square")
player.shapesize(5, 1)
player.penup()
player.goto(560, 0)

player2 = turtle.Turtle()
player2.color("white")
player2.shape("square")
player2.shapesize(5, 1)
player2.penup()
player2.goto(-560, 0)

ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

scoretext = turtle.Turtle()
scoretext.hideturtle()
scoretext.color("white")
scoretext.penup()
scoretext.goto(0, 300)
scoretext.write("Pong", align="center", font=("Arial", 24, "bold"))

dx = 2
dy = 2
keep_playing = True

def player_up():
    if player.ycor() < 300:
        player.sety(player.ycor() + 25)

def player_down():
    if player.ycor() > -300:
        player.sety(player.ycor() - 25)

def player2_up():
    if player2.ycor() < 300:
        player2.sety(player2.ycor() + 25)

def player2_down():
    if player2.ycor() > -300:
        player2.sety(player2.ycor() - 25)

win.listen()
win.onkeypress(player_up, "Up")
win.onkeypress(player_down, "Down")
win.onkeypress(player2_up, "w")
win.onkeypress(player2_down, "s")

def bounce_right():
    global dx
    if ball.xcor() > 540 and player.ycor()-50 < ball.ycor() < player.ycor()+50:
        dx = -dx
        ball.setx(540)

def bounce_left():
    global dx
    if ball.xcor() < -540 and player2.ycor()-50 < ball.ycor() < player2.ycor()+50:
        dx = -dx
        ball.setx(-540)

while keep_playing:
    win.update()

    ball.setx(ball.xcor() + dx)
    ball.sety(ball.ycor() + dy)

    if ball.ycor() > 330 or ball.ycor() < -330:
        dy = -dy

    if ball.xcor() > 590 or ball.xcor() < -590:
        keep_playing = False
        scoretext.goto(0, 0)
        scoretext.write("GAME OVER", align="center", font=("Arial", 36, "bold"))

    bounce_right()
    bounce_left()

    time.sleep(0.01)