import turtle

# הגדרות מסך
screen = turtle.Screen()
screen.setup(600, 700)
screen.bgcolor("#fdf6e3")  # רקע בצבע קרם נעים
t = turtle.Turtle()
t.speed(3)  # מהירות בינונית
t.pensize(4)

# צבעים
SKIN_COLOR = "#ffe0bd"  # צבע עור בהיר
SHIRT_COLOR = "#268bd2" # כחול
PANTS_COLOR = "#dc322f" # אדום
HAIR_COLOR = "#657b83" # אפור-חום
EYE_COLOR = "#073642" # כחול כהה מאוד

def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_filled_circle(x, y, radius, color):
    move_to(x, y - radius)
    t.color(color, color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# --- 1. ראש ושיער ---
print("מצייר ראש...")
draw_filled_circle(0, 200, 50, SKIN_COLOR)

# שיער (קווים פשוטים)
t.color(HAIR_COLOR)
t.pensize(6)
for angle in range(45, 136, 15):
    move_to(0, 230)
    t.setheading(angle)
    t.forward(35)
t.pensize(4)

# --- 2. פנים (עיניים וחיוך) ---
print("מצייר פנים...")
# עין שמאל
draw_filled_circle(-20, 210, 6, EYE_COLOR)
# עין ימין
draw_filled_circle(20, 210, 6, EYE_COLOR)

# חיוך (קשת)
move_to(-25, 185)
t.setheading(-60)
t.color(EYE_COLOR)
t.circle(30, 120)

# --- 3. גוף (חולצה) ---
print("מצייר גוף...")
move_to(-50, 150)
t.color(SHIRT_COLOR, SHIRT_COLOR)
t.begin_fill()
t.setheading(0)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.end_fill()

# --- 4. מכנסיים ---
print("מצייר מכנסיים...")
move_to(-50, 50)
t.color(PANTS_COLOR, PANTS_COLOR)
t.begin_fill()
t.setheading(0)
t.forward(45)  # רגל שמאל
t.right(90)
t.forward(60)
t.right(90)
t.forward(45)
t.end_fill()

move_to(5, 50)
t.begin_fill()
t.setheading(0)
t.forward(45)  # רגל ימין
t.right(90)
t.forward(60)
t.right(90)
t.forward(45)
t.end_fill()

# --- 5. ידיים ---
print("מצייר ידיים...")
t.color(SKIN_COLOR)
t.pensize(8)
# יד שמאל (מונפת לשלום)
move_to(-50, 140)
t.setheading(140)
t.forward(70)
# כף יד שמאל
draw_filled_circle(t.xcor(), t.ycor(), 10, SKIN_COLOR)

# יד ימין (למטה)
t.pensize(8)
t.color(SKIN_COLOR)
move_to(50, 140)
t.setheading(-40)
t.forward(70)
# כף יד ימין
draw_filled_circle(t.xcor(), t.ycor(), 10, SKIN_COLOR)

# --- 6. כיתוב ---
t.color("black")
move_to(-260, -80)
t.write("המשיכו את הסדרה"+": s,m,t,w,t,f,...", font=("Arial", 20, "bold"))


t.hideturtle()
turtle.done()
