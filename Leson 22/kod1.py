import turtle

# הגדרות מסך וצב
screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("#f0f0f0")


t = turtle.Turtle()
t.pensize(3)
t.speed(0) # מהירות מקסימלית לציור

# צבעים
PIKACHU_YELLOW = "#F6E05E"
PIKACHU_RED = "#E53E3E"
BLACK = "#2D3748"
WHITE = "#FFFFFF"

# פונקציית עזר להזזת הצב ללא ציור
def move_to(x, y):
   t.penup()
   t.goto(x, y)
   t.pendown()

# 1. ציור הראש (עיגול צהוב גדול)
move_to(0, -100)
t.color(BLACK, PIKACHU_YELLOW)
t.begin_fill()
t.setheading(0)
t.circle(150)
t.end_fill()

# 2. ציור האוזן השמאלית
move_to(-120, 110)
t.setheading(130)
t.begin_fill()
# קשת חיצונית
t.circle(200, 30)
# קצה האוזן (שחור)
t.color(BLACK, BLACK)
t.circle(30, 150)
t.end_fill()
# המשך האוזן חזרה לראש
t.color(BLACK, PIKACHU_YELLOW)
t.begin_fill()
t.setheading(330)
t.circle(-200, 35)
t.goto(-120, 110)
t.end_fill()

# 3. ציור האוזן הימנית
move_to(120, 110)
t.setheading(50)
t.begin_fill()
# קשת חיצונית
t.circle(-200, 30)
# קצה האוזן (שחור)
t.color(BLACK, BLACK)
t.circle(-30, 150)
t.end_fill()
# המשך האוזן חזרה לראש
t.color(BLACK, PIKACHU_YELLOW)
t.begin_fill()
t.setheading(210)
t.circle(200, 35)
t.goto(120, 110)
t.end_fill()

# 4. ציור העין השמאלית
move_to(-60, 50)
t.color(BLACK, BLACK)
t.begin_fill()
t.setheading(0)
t.circle(25)
t.end_fill()
# אישון (לבן)
move_to(-50, 65)
t.color(WHITE, WHITE)
t.begin_fill()
t.circle(8)
t.end_fill()

# 5. ציור העין הימנית
move_to(60, 50)
t.color(BLACK, BLACK)
t.begin_fill()
t.setheading(0)
t.circle(25)
t.end_fill()
# אישון (לבן)
move_to(70, 65)
t.color(WHITE, WHITE)
t.begin_fill()
t.circle(8)
t.end_fill()

# 6. ציור האף
move_to(0, 20)
t.color(BLACK, BLACK)
t.begin_fill()
t.setheading(-60)
t.circle(5, steps=3) # אף משולש
t.end_fill()

# 7. ציור הפה (שתי קשתות)
move_to(-30, -10)
t.color(BLACK)
t.setheading(-60)
t.circle(35, 120) # קשת שמאלית
t.setheading(-60)
t.circle(35, 120) # קשת ימנית

# 8. ציור הלחיים (עיגולים אדומים)
# לחי שמאלית
move_to(-130, -20)
t.color(PIKACHU_RED, PIKACHU_RED)
t.begin_fill()
t.setheading(0)
t.circle(35)
t.end_fill()
# לחי ימנית
move_to(130, -20)
t.color(PIKACHU_RED, PIKACHU_RED)
t.begin_fill()
t.setheading(0)
t.circle(35)
t.end_fill()


t.hideturtle()
screen.exitonclick()