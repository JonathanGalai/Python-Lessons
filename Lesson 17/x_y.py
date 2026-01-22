import turtle

def closest_distance(player1, player2):
    if player1.distance(0, 0) > player2.distance(0, 0):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")


sc = turtle.Screen()
sc.setup(1000, 1000)

player1 = turtle.Turtle()
player1.shape('turtle')
player1.color('red')

player2 = turtle.Turtle()
player2.shape('turtle')
player2.color('red')



x_player1 = int(input("Choose x for player 1:\n"))
y_player1 = int(input("Choose y for player 1:\n"))
x_player2 = int(input("Choose x for player 2:\n"))
y_player2 = int(input("Choose y for player 2:\n"))

player1.goto(x_player1, y_player1)
player2.goto(x_player2, y_player2)

print(closest_distance(player1, player2))
turtle.done()