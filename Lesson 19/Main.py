import turtle
import random
import time

win = turtle.Screen()
win.bgcolor("beige")
win.setup(600, 800)
win.tracer(0)

# Question turtle
player_question = turtle.Turtle()
player_question.hideturtle()
player_question.penup()

# Answer turtles
player_ans = turtle.Turtle()
player_ans.hideturtle()
player_ans.penup()

player_ans1 = turtle.Turtle()
player_ans1.hideturtle()
player_ans1.penup()

player_ans2 = turtle.Turtle()
player_ans2.hideturtle()
player_ans2.penup()

# Random numbers
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
right_ans = num1 + num2
random1 = random.randint(1, 150)
random2 = random.randint(1, 150)

# Show question
player_question.goto(0, 350)
player_question.write(f"{num1} + {num2}", align="center", font=("Arial", 24, "bold"))

# Starting positions
player_ans.goto(0, 200)
player_ans1.goto(-150, 200)
player_ans2.goto(150, 200)

# Winner / loser functions
def winner():
    player_question.clear()
    player_question.write("You Won!", align="center", font=("Arial", 24, "bold"))

def loser():
    player_question.clear()
    player_question.write("You Lose!", align="center", font=("Arial", 24, "bold"))

# Function to check click
def check_click(x, y, value):
    if value == right_ans:
        winner()
    else:
        loser()

# Attach clicks
player_ans.onclick(lambda x, y: check_click(x, y, right_ans))
player_ans1.onclick(lambda x, y: check_click(x, y, random1))
player_ans2.onclick(lambda x, y: check_click(x, y, random2))

# Simple move function
def move_down(turtle_obj, value):
    turtle_obj.clear()
    turtle_obj.write(value, align="center", font=("Arial", 18, "bold"))
    turtle_obj.sety(turtle_obj.ycor() - 20)
    time.sleep(0.05)

# Falling animation
for i in range(25):
    move_down(player_ans, right_ans)
    move_down(player_ans1, random1)
    move_down(player_ans2, random2)
    win.update()

win.mainloop()
