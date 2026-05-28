import turtle
t = turtle.Turtle()
t.pensize(5)

t.left(90)        # שינוי ל-90 (קו אנכי)
t.forward(100)
t.right(90)
t.forward(50)
t.backward(100)
t.forward(50)
t.right(90)
t.forward(100)
t.right(90)
t.setheading(-90)
t.circle(-45, 135)


turtle.done()