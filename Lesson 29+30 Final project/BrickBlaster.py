import turtle
import time

# Window setup
win = turtle.Screen()
win.setup(width=1280, height=720)
win.bgcolor("black")
win.title("Brick Blaster")
win.tracer(0)

# Paddle (bottom)
player = turtle.Turtle()
player.shape("square")
player.color("white")
player.shapesize(stretch_wid=1, stretch_len=6)
player.penup()
player.goto(0, -300)

# Brick
bricks = []

colors = ["red", "orange", "yellow", "green"]
start_x = -500
start_y = 250

for row in range(4):
    for col in range(10):

        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(colors[row])
        brick.shapesize(stretch_wid=1, stretch_len=4)
        brick.penup()

        x = start_x + (col * 110)
        y = start_y - (row * 40)

        brick.goto(x, y)

        bricks.append(brick)


# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Text
scoretext = turtle.Turtle()
scoretext.hideturtle()
scoretext.color("white")
scoretext.penup()
scoretext.goto(0, 300)

# Ball speed
dx = 5
dy = -5

score = 0

keep_playing = True

# Paddle movement
def move_left():
    x = player.xcor()
    if x > -540:
        player.setx(x - 30)

def move_right():
    x = player.xcor()
    if x < 540:
        player.setx(x + 30)

# Keyboard controls
win.listen()
win.onkeypress(move_left, "Left")
win.onkeypress(move_right, "Right")

# Main game loop
while keep_playing:
    win.update()

    # Move ball
    ball.setx(ball.xcor() + dx)
    ball.sety(ball.ycor() + dy)

    # Bounce off left/right walls
    if ball.xcor() > 620:
        ball.setx(620)
        dx *= -1

    if ball.xcor() < -620:
        ball.setx(-620)
        dx *= -1

    # Bounce off top wall
    if ball.ycor() > 340:
        ball.sety(340)
        dy *= -1

    # Paddle collision
    if (
        -320 < ball.ycor() < -290
        and player.xcor() - 60 < ball.xcor() < player.xcor() + 60
    ):
        ball.sety(-290)
        dy *= -1

    # Brick collisions
    for brick in bricks:

        if brick.isvisible():

            if ball.distance(brick) < 45:

                brick.hideturtle()

                # Add score
                score += 1

                # Update text
                scoretext.clear()
                scoretext.write(
                    f"Score: {score}",
                    align="center",
                    font=("Arial", 24, "bold")
                )

                dy *= -1
                break

    # Game over
    if ball.ycor() < -360:
        keep_playing = False
        scoretext.goto(0, 0)
        scoretext.write(
            "GAME OVER",
            align="center",
            font=("Arial", 36, "bold")
        )

    time.sleep(0.01)

win.mainloop()