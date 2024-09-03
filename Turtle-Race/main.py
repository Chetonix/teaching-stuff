import random
from turtle import Turtle, Screen

POSITIONS = [(-280, 300), (-280, 200), (-280, 100), (-280,0), (-280, -100), (-280, -200), (-280, -300)]
COLORS = ["blue","red","purple","orange","yellow","green","violet"]

wn = Screen()
wn.setup(600, 700)

all_turtles = []
for i in range(7):
    che = Turtle()
    che.penup()
    che.shape("turtle")
    che.goto(POSITIONS[i])
    che.color(COLORS[i])
    all_turtles.append(che)

won = False

#color = input("Choose a color of the turtle you bet! ")
color = wn.textinput(title="Make a bet",
                            prompt="Whick turtle is gonna win the race?: ")

while True:
    for che in all_turtles:
        move_distance = random.randint(1, 10)
        che.forward(move_distance)
    
        if che.xcor() > 280:
            won = True
            print(f"The turtle with {che.fillcolor()} won the game!")
            if che.fillcolor() == color.lower():
                print("You won!")
            else:
                print("You lost!")
    if won:
        break
    
wn.exitonclick()