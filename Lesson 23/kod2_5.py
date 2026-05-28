import turtle

# הגדרות מסך
screen = turtle.Screen()
screen.setup(800, 500)
screen.bgcolor("#222222")  # רקע כהה כדי שהגפרורים "יידלקו"
screen.title("חידת הגפרורים האחרונה!")

t = turtle.Turtle()
t.speed(0)  # מהירות מקסימלית לציור
t.pensize(2)
t.hideturtle()

# צבעים
MATCH_COLOR = "#FFD700"  # זהב (כמו גפרור דולק)
TIP_COLOR = "#FF4500"  # אדום-כתום (ראש הגפרור)


def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def draw_match(x, y, angle, length=40):
    """מצייר גפרור בודד במיקום ובזווית נתונה"""
    move_to(x, y)
    t.setheading(angle)

    # גוף הגפרור
    t.color(MATCH_COLOR)
    t.pensize(4)
    t.forward(length - 5)

    # ראש הגפרור (אדום)
    t.color(TIP_COLOR)
    t.pensize(6)
    t.forward(5)
    t.pensize(2)


def draw_digit(x, y, digit):
    """מצייר ספרת גפרורים (0-9) במיקום x,y"""
    # הגדרות מיקום לגפרורים (אנכיים ואופקיים)
    gap = 5  # רווח קטן בין גפרורים
    L = 40  # אורך גפרור

    # מפה של אילו גפרורים (מתוך 7) דולקים עבור כל ספרה
    # סדר הגפרורים: [עליון, אמצעי, תחתו', שמאלי-עליון, ימני-עליון, שמאלי-תחתון, ימני-תחתון]
    segments = {
        '0': [1, 0, 1, 1, 1, 1, 1],
        '1': [0, 0, 0, 0, 1, 0, 1],
        '2': [1, 1, 1, 0, 1, 1, 0],
        '3': [1, 1, 1, 0, 1, 0, 1],
        '4': [0, 1, 0, 1, 1, 0, 1],
        '5': [1, 1, 1, 1, 0, 0, 1],
        '6': [1, 1, 1, 1, 0, 1, 1],
        '7': [1, 0, 0, 0, 1, 0, 1],
        '8': [1, 1, 1, 1, 1, 1, 1],
        '9': [1, 1, 1, 1, 1, 0, 1],
        '+': [0, 1, 0, 0, 0, 0, 0],  # רק האמצעי לסימן פלוס אנכי
        '-': [0, 1, 0, 0, 0, 0, 0],  # רק האמצעי לסימן מינוס
        '=': [0, 1, 0, 0, 0, 0, 0]  # נצייר שניים ידנית
    }

    if digit not in segments: return

    seg = segments[digit]

    # גפרורים אופקיים
    if seg[0]: draw_match(x + gap, y + 2 * L + 2 * gap, 0, L)  # עליון
    if seg[1]: draw_match(x + gap, y + L + gap, 0, L)  # אמצעי
    if seg[2]: draw_match(x + gap, y, 0, L)  # תחתוון

    # גפרורים אנכיים
    if seg[3]: draw_match(x, y + L + gap, 90, L)  # שמאלי-עליון
    if seg[4]: draw_match(x + L + 2 * gap, y + L + gap, 90, L)  # ימני-עליון
    if seg[5]: draw_match(x, y, 90, L)  # שמאלי-תחתון
    if seg[6]: draw_match(x + L + 2 * gap, y, 90, L)  # ימני-תחתון


def draw_plus(x, y):
    """מצייר סימן פלוס מגפרורים"""
    L = 40
    gap = 5
    # אופקי
    draw_match(x + gap, y + L + gap, 0, L)
    # אנכי (מרכזי)
    draw_match(x + L / 2 + gap, y + gap / 2, 90, 2 * L + 2 * gap)


def draw_equals(x, y):
    """מצייר סימן שווה מגפרורים"""
    L = 40
    gap = 5
    draw_match(x + gap, y + L + gap + 10, 0, L)  # קו עליון
    draw_match(x + gap, y + L + gap - 10, 0, L)  # קו תחתוון


# --- שלבי הציור של המשוואה: 8 + 3 = 9 ---

print("מצייר את חידת הגפרורים... תקשיבו טוב...")
start_x = -350
y_pos = -50
space = 100

# 1. ספרה 8
draw_digit(start_x, y_pos, '8')

# 2. סימן +
draw_plus(start_x + space, y_pos)

# 3. ספרה 3
draw_digit(start_x + 2 * space, y_pos, '3')

# 4. סימן =
draw_equals(start_x + 3 * space, y_pos)

# 5. ספרה 9
draw_digit(start_x + 4 * space, y_pos, '9')

# --- הכיתוב של החידה ---
t.color("white")
move_to(-200, -150)
t.write("הזיזו גפרור אחד בלבד", font=("Arial", 24, "bold"))
move_to(-180, -200)
t.write("כדי שהמשוואה תהיה נכונה!", font=("Arial", 20, "normal"))

print("סיימתי! בהצלחה בפתרון.")
t.hideturtle()
turtle.done()
