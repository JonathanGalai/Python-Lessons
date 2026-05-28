import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.pensize(2)
# רשימת צבעים
colors = ["red", "purple", "blue", "green", "orange", "yellow"]

# לולאת הציור
for i in range(200):
    t.color(colors[i % 6])
    t.forward(i * 1.5)

    t.left(120)

t.hideturtle()
turtle.done()
