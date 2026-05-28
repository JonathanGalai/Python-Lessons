import turtle
t = turtle.Turtle()
t.pensize(4)
t.speed(0)
t.shape("blank")

angle = 1
for i in range(360):
    t.forward(1)
    t.right(angle)

turtle.mainloop()