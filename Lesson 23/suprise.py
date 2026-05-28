import turtle
import time
import base64




def clear_board():
    global current_column
    global current_row
    time.sleep(2)
    end_word_player.reset()
    current_column = 0
    current_row = 0
    player_squares.clear()
    build_squares()
    new_word()

def end_word(num):
    global word
    end_word_player.pu()
    end_word_player.goto(-200, -100)

    if num ==0:

        text = "YOU LOSE:((  the word is " + word
        end_word_player.write(text, font=('arial',23,'normal'))
        clear_board()
    else:
        # update score
        end_word_player.write('GREAT!', font=('arial', 23, 'normal'))
        clear_board()
    player.pd()



def check_word(current_row):
    global word_list
    right_word = True
    if line_filled:
        for i in range (5):
            if (letter_board[current_row][i] == word_list[i]) :
                color_square("lightgreen",current_row,i)
            elif letter_board[current_row][i] in word_list:
                color_square("gold",current_row,i)
                right_word = False
            else:
                color_square("grey",current_row,i)
                right_word = False
        return right_word

def fill_letter(x,y):
    global choise
    global game_started
    global start_player
    if not game_started:
        if -50>x>-150 and -20>y>-70:
            choise = 1
        if 150>x>50 and -20>y>-70:
            choise = 2
        start_player.reset()
        for x, y in thisdict.items():
            build_square_letter(y)
            player.forward(10)
            player.write(x, font=('ariel', 18, 'normal'))
        build_big_square((-250, -270), 'Enter')
        build_big_square((175, -270), 'Back')
        game_started = True
        build_squares()
        new_word()
        return
    global current_letter
    global current_column
    global current_row
    global line_filled
    global continue_playing
    if -250<x<-215  and -270<y<-225 and line_filled == True:
        if check_word(current_row):
            line_filled = False
            end_word(1)
            return

        if current_row < 5:
            current_row = current_row + 1
            #current_column = 0
            line_filled = False
        else:
            end_word(0)
        return
    for letter, location in thisdict.items():
        loc_x, loc_y = location
        if (loc_x<x<loc_x+35) and (loc_y<y<loc_y+45) :
            current_letter = letter
            letter_board[current_row][current_column] = current_letter
            player_squares.pu()
            player_squares.goto(-150+55*current_column,250-55*current_row)
            player_squares.forward(17)
            player_squares.write(current_letter,font=('Ariel',18,'normal'))
            if current_column < 4:
                current_column = current_column+1
            else:
                line_filled=True
                #line_filled_num = current_column
                current_column=0


def build_big_square(tup,type):
    x, y = tup
    player.pu()
    player.begin_fill()
    player.goto(x, y)
    player.pd()
    player.forward(55)
    player.left(90)
    player.forward(45)
    player.left(90)
    player.forward(55)
    player.left(90)
    player.forward(45)
    player.left(90)
    player.end_fill()
    if type == 'Enter':
        player.write('Enter',font=('arial',16,'normal'))
    else:
        player.pu()
        player.goto(195,-257)
        player.pd()
        player.forward(20)
        player.left(90)
        player.forward(20)
        player.left(90)
        player.forward(20)
        player.left(45)
        player.forward(14)
        player.left(90)
        player.forward(14)
        #player.left(45)
        player.pu()
        player.goto(198,-241)
        player.pd()
        player.forward(15)
        player.pu()
        player.left(135)
        player.forward(10)
        player.pd()
        player.left(135)
        player.forward(15)
        player.left(135)

def color_square(color,i,j):
    player_squares.pu()
    player_squares.goto(-150 + j*55, 250 - i*55)
    player_squares.pd()
    player_squares.fillcolor(color)
    player_squares.begin_fill()
    for x in range(1, 5):
        player_squares.forward(45)
        player_squares.left(90)
    player_squares.end_fill()
    player_squares.forward(17)
    player_squares.write(letter_board[i][j], font=('Ariel', 18, 'normal'))

def build_squares():
    for i in range(0,250,55):
        for j in range(0,320,55):
            player_squares.pu()
            player_squares.goto(-150+i,250-j)
            player_squares.pd()
            for x in range (1,5):
                player_squares.forward(45)
                player_squares.left(90)

def build_square_letter(tup):
    x,y = tup
    player.pu()
    player.begin_fill()
    player.goto(x,y)
    player.pd()
    player.forward(35)
    player.left(90)
    player.forward(45)
    player.left(90)
    player.forward(35)
    player.left(90)
    player.forward(45)
    player.left(90)
    player.end_fill()




def new_word():
    global word
    global word_list
    word_list = []
    word = "HIIII"
    for letter in word:
        word_list.append(letter)
    word.replace("\n", "")


def start_game():
    start_player.shape('blank')
    start_player.fillcolor('cyan')
    start_player.pu()
    start_player.goto(-200, -100)
    start_player.setheading(90)

ENCRYPTED_CODE = "MTcyNDEyMFMw"
wn = turtle.Screen()
wn.bgcolor("beige")
turtle.shape('blank')
player = turtle.Turtle()
player.shape('blank')
player.speed(0)
player.pensize(2)
player.fillcolor("lightgrey")
player_squares = turtle.Turtle()
player_squares.shape('blank')
player_squares.speed(0)
player_squares.pensize(2)
start_player = turtle.Turtle()
start_player.speed(0)
start_player.shape('blank')

thisdict = {
  "Q": (-250,-150), "W": (-200,-150), "E": (-150,-150), "R": (-100,-150), "T": (-50,-150), "Y": (0,-150), "U": (50,-150), "I": (100,-150), "O": (150,-150), "P": (200,-150),
"A": (-225,-210), "S": (-175,-210), "D": (-125,-210), "F": (-75,-210), "G": (-25,-210), "H": (25,-210), "J": (75,-210), "K": (125,-210), "L": (175,-210),
"Z": (-175,-270), "X": (-125,-270), "C": (-75,-270), "V": (-25,-270), "B": (25,-270), "N": (75,-270), "M": (125,-270)
}
color_board = [["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""]]
letter_board = [["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""]]
current_letter=""
game_started=False
player.pensize(1)
player.shape('blank')

current_column = 0
current_row = 0
line_filled=False
line_filled_num = 0
continue_playing = True
word=""
word_list = []
end_word_player = turtle.Turtle()
end_word_player.shape('blank')

wn.onclick(fill_letter)


def check_code():
    print("--- מערכת אבטחה מוצפנת ---")

    # קבלת קלט מהמשתמש
    user_input = input("נא להזין קוד סודי: ").strip()

    # הצפנת הקלט של המשתמש כדי להשוות אותו לקוד השמור
    user_input_encoded = base64.b64encode(user_input.encode()).decode()

    if user_input_encoded == ENCRYPTED_CODE:
        print("\n✅ פיצוח הקוד הושלם! המערכת פתוחה.")
        start_game()
    else:
        print("\n❌ הגישה נדחתה. הקוד אינו תואם למפתח ההצפנה.")



# הפעלת הבדיקה
check_code()
#start_game()

turtle.mainloop()