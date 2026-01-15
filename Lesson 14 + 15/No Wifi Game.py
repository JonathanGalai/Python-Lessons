import turtle
import random
import time

sc = turtle.Screen()
sc.bgcolor("beige")
sc.setup(1000, 900)

sc.register_shape("dino.gif")
sc.register_shape("dino2.gif")
sc.register_shape("dino2.gif")
sc.register_shape("plant.gif")
sc.register_shape("plant2.gif")

dino = turtle.Turtle()
dino_image = 'dino.gif'
dino.pu()
dino.shape(dino_image)
dino.goto(-400, -350)

# צמחים
plant = turtle.Turtle()
plant_image = 'plant.gif'
plant.shape(plant_image)
plant.pu()
plant.goto(1100, -350)
continue_playing = True
score = 0

plant2 = turtle.Turtle()
plant2.shape("plant2.gif")
plant2.pu()
plant2.goto(1100, -350)
plant2.speed(3)

# קפיצה גבוהה
def jump():
    for i in range(20):
        dino.setpos(dino.xcor(), dino.ycor() + 15)
        plant.back(10)

    for i in range(20):
        dino.setpos(dino.xcor(), dino.ycor() - 15)
        plant.back(10)


# קישורים למקשים
turtle.listen()
turtle.onkey(jump, "space")
turtle.onkey(jump, "Up")

# לולאה ראשית
while continue_playing:
    if plant.xcor() < -550:
        score += 1
        plant.speed(10)
        plant.hideturtle()
        plant.setpos(500, -350)
        plant.showturtle()
        plant.speed(2)
    else:
        plant.back(10)

    if score == 5:
        sc.bgcolor("red")

    if dino_image == 'dino.gif':
        dino_image = 'dino1.gif'
        dino.shape = (dino_image)
    elif dino_image == 'dino1.gif':
        dino_image = 'dino2.gif'
        dino.shape = (dino_image)
    elif dino_image == 'dino2.gif':
        dino_image = 'dino.gif'
        dino.shape = (dino_image)

    #check
        if dino.ycor() == -350 and plant.xcor() - dino.xcor() <50 and plant.xcor() > dino.xcor():
            print("plant" + str(plant.xcor()))
            print("dino" + str(dino.xcor()))
            continue_playing = False
            message = "Game Over! your score is " + str(score)
            dino.goto(0, 0)
            dino.write(message, font = ('arial', 18, 'normal'))
turtle.mainloop()
