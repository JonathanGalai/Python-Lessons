import turtle
sc = turtle.Screen()
sc.bgcolor('beige')
sc.setup(800,800)
hanging_stage = 0
right_answers = 0
#questions
question = turtle.Turtle()
question.shape('blank')
question.pu()
question.goto(-200,300)
question.write("כמה זה 100+1300")

#the lines
line = turtle.Turtle()
line.shape('blank')
line.pensize(4)

for i in range(4):
    line.forward(50)
    line.pu()
    line.forward(40)
    line.pd()
line.pu()
line.goto(-200,250)
line.pd()
line.goto(-200,280)
line.goto(-180,280)
line.goto(-300,280)
line.goto(-280,280)
line.goto(-280,0)
line.goto(-200,0)
line.goto(-300,0)
line.goto(-100,0)
line.pu()
line.goto(-200,250)
line.pd()

def one():
    global right_answers
    right_answers = right_answers + 1
    line.pu()
    line.goto(25,0)
    line.write('1', font = ('Arial', 18, 'normal'))
    if right_answers == 4:
        line.pu()
        line.goto(0,200)
        line.write("Great!", font = ("Arial", 28, 'normal'))
def zero():
    global right_answers
    right_answers = right_answers + 1
    line.pu()
    line.goto(115,0)
    line.write('0', font = ('Arial', 18, 'normal'))
    if right_answers == 4:
        line.pu()
        line.goto(0,200)
        line.write("Great!", font = ("Arial", 28, 'normal'))
def two():
    global right_answers
    right_answers = right_answers + 1
    line.pu()
    line.goto(205,0)
    line.write('0', font = ('Arial', 18, 'normal'))
    if right_answers == 4:
        line.pu()
        line.goto(0,200)
        line.write("Great!", font = ("Arial", 28, 'normal'))
def three():
    global right_answers
    right_answers = right_answers + 1
    line.pu()
    line.goto(295,0)
    line.write('0', font = ('Arial', 18, 'normal'))
    if right_answers == 4:
        line.pu()
        line.goto(0,200)
        line.write("Great!", font = ("Arial", 28, 'normal'))
def other():
    global hanging_stage
    if hanging_stage == 0:
        line.goto(-200,250)
        line.pd()
        line.rt(180)
        line.circle(50)
        line.pu()
        hanging_stage = hanging_stage + 1
    elif hanging_stage == 1:
        line.goto(-200,150)
        line.pd()
        line.goto(-250,100)
        line.pu()
        hanging_stage = hanging_stage + 1
    elif hanging_stage == 2:
        line.goto(-200, 150)
        line.pd()
        line.goto(-150, 100)
        line.pu()
        hanging_stage = hanging_stage + 1
    elif hanging_stage == 3:
        line.goto(-200, 150)
        line.pd()
        line.goto(-200, 100)
        line.pu()
        hanging_stage = hanging_stage + 1
    elif hanging_stage == 4:
        line.goto(-200, 100)
        line.pd()
        line.goto(-250, 50)
        line.pu()
        hanging_stage = hanging_stage + 1
    elif hanging_stage == 5:
        line.goto(-200, 100)
        line.pd()
        line.goto(-150, 50)
        line.pu()
        hanging_stage = hanging_stage + 1
    else:
        line.pu()
        line.goto(0,200)
        line.write("FAIL!", font = ("Arial", 28, 'normal'))

turtle.listen()
turtle.onkey(zero, 0)
turtle.onkey(two, 2)
turtle.onkey(three, 3)
turtle.onkey(other, 4)
turtle.onkey(other, 5)
turtle.onkey(other, 6)
turtle.onkey(other, 7)
turtle.onkey(other, 8)
turtle.onkey(other, 9)


turtle.mainloop()