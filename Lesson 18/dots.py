import turtle

player = turtle.Turtle()
player.shape('turtle')

win = turtle.Screen()
win.bgcolor('white')
win.setup(800, 600)
def dots(x, y):
    player.pu()
    player.goto(x, y)
    player.pd()
    player.circle(50, 360)

win.onclick(dots)
turtle.mainloop()