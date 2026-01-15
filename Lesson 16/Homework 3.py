import turtle

sc = turtle.Screen()
sc.bgcolor("beige")
sc.setup(1000, 900)

t = turtle.Turtle()
t.shape("turtle")
t.color("black")
t.speed(2)

side = int(sc.textinput("Side", "Enter number for the side:"))

t.goto(0, 0)
for i in range(5):
    t.forward(side)
    t.left(72)

turtle.done()
