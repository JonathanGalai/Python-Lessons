import turtle
import math

# הגדרות מסך
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.color("red")
t.pensize(3)


def draw_heart():
    t.begin_fill()
    # נוסחה מתמטית ללב (X ו-Y כפונקציה של t)
    for i in range(0, 62):
        # זווית ברדיאנים
        angle = i * 0.1

        # נוסחת הלב המפורסמת
        x = 16 * math.sin(angle) ** 3
        y = 13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)

        t.goto(x * 7, y * 7)

    t.end_fill()


# הזזה לנקודת התחלה בלי להשאיר קו
t.penup()
t.goto(0, 0)
t.pendown()

draw_heart()

t.hideturtle()
turtle.done()
