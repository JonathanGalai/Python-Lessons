import turtle
import random

# ------------------ Window ------------------
win = turtle.Screen()
win.bgcolor("beige")
win.setup(600, 800)
win.tracer(0)

# ------------------ Score ------------------
score = 0
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(0, 370)

def update_score():
    score_writer.clear()
    score_writer.write(f"Score: {score}/3", align="center",
                       font=("Arial", 20, "bold"))

update_score()

# ------------------ Question ------------------
question_writer = turtle.Turtle()
question_writer.hideturtle()
question_writer.penup()
question_writer.goto(0, 330)

# ------------------ Create Answer ------------------
def create_answer(x_pos):
    square = turtle.Turtle()
    square.shape("square")
    square.shapesize(2, 5)
    square.color("black", "lightblue")
    square.penup()
    square.goto(x_pos, 250)

    text = turtle.Turtle()
    text.hideturtle()
    text.penup()

    return square, text

answers = [
    create_answer(-200),
    create_answer(0),
    create_answer(200)
]

# ------------------ Generate New Round ------------------
def new_round():
    global num1, num2, right_ans, values

    question_writer.clear()

    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    right_ans = num1 + num2

    wrong1 = random.randint(1, 100)
    wrong2 = random.randint(1, 100)

    while wrong1 == right_ans:
        wrong1 = random.randint(1, 100)

    while wrong2 == right_ans or wrong2 == wrong1:
        wrong2 = random.randint(1, 100)

    values = [right_ans, wrong1, wrong2]
    random.shuffle(values)

    question_writer.write(f"{num1} + {num2}",
                          align="center",
                          font=("Arial", 28, "bold"))

    for i in range(3):
        square, text = answers[i]
        square.goto([-200, 0, 200][i], 250)
        text.clear()

new_round()

# ------------------ Click Logic ------------------
def check_answer(clicked_value):
    global score

    if clicked_value == right_ans:
        score += 1
        update_score()

        if score >= 3:
            question_writer.clear()
            question_writer.write("🎉 You Win The Game!",
                                  align="center",
                                  font=("Arial", 28, "bold"))
            return

    new_round()

# Attach clicks
for i in range(3):
    square, text = answers[i]
    square.onclick(lambda x, y, i=i: check_answer(values[i]))

# ------------------ Falling Animation ------------------
def fall():
    for i in range(3):
        square, text = answers[i]

        square.sety(square.ycor() - 4)

        text.clear()
        text.goto(square.xcor(), square.ycor() - 10)
        text.write(values[i],
                   align="center",
                   font=("Arial", 18, "bold"))

    win.update()

    if score < 3:
        win.ontimer(fall, 20)

fall()

win.mainloop()
