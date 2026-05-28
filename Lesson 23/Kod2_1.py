import turtle

t = turtle.Turtle()
t.penup()
t.goto(-200,0)
t.pendown()
t.shape('blank')
t.color("green")
t.pensize(3)

steps = [60, 20, 30, 40, 50]


for i in range(22):
    move = steps[i % 5]
    t.forward(move)
    t.right(90)

turtle.mainloop()