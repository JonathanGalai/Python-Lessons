import turtle

t = turtle.Turtle()
t.speed(3)
t.pensize(3)
turtle.bgcolor("black")
t.color("yellow")

# הזזת הצב לנקודת התחלה נוחה
t.penup()
t.goto(-100, -50)
t.pendown()

# הלולאה החיצונית - מציירת 3 משולשים גדולים
# זהו הצופן לחדר הבריחה!
for i in range(9):
    # ציור משולש שווה צלעות
    for side in range(3):
        t.forward(200)
        t.left(120)

    # סיבוב של 40 מעלות לפני המשולש הבא
    # זה מה שיוצר את החפיפה המבלבלת
    t.left(40)

t.hideturtle()
turtle.done()
