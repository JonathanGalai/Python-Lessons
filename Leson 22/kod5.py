import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

# רשימת צבעים שחוזרת על עצמה
colors = ["#FF5733", "#33FF57", "#3357FF", "#F333FF"]

# הגדרה ראשונית
count = 0

# לולאה ראשונה: כמה "קבוצות" של עיגולים יש?
for i in range(13):
    t.color(colors[i % 4])

    # לולאה שנייה: כמה עיגולים בכל קבוצה?
    for j in range(i+1):
        t.penup()
        t.forward(10)  # תנועה קטנה קדימה יוצרת חפיפה
        t.left(4)  # סיבוב קל יוצר את הספירלה
        t.pendown()

        t.circle(40)  # הציור עצמו
        count += 1  # מונה פנימי סודי

t.hideturtle()
turtle.done()