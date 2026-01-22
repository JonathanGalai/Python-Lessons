import turtle

sc = turtle.Screen()
sc.setup(1000, 1000)

player = turtle.Turtle()
player.color('black')
player.speed(1)
player.penup()


def in_screen(x, y, turtle):
    if player.distance(x, y) > 500:
        print("The turtle isn't in the screen")
    else:
        print("The turtle is in the screen")



x = int(input("Enter the x coordinate: "))
y = int(input("Enter the y coordinate: "))

player.goto(x, y)
print(in_screen(x, y, player))