from turtle import Turtle, Screen
import random

wn = Screen()
wn.setup(600, 600)

che = Turtle()
che.shape("turtle")

while(True):

    random_move = random.randint(5, 50)
    random_turn = random.randint(0, 360)

    if che.xcor() > 280:
        che.setheading(180)
        che.forward(100)

    if che.ycor() > 280:
        che.setheading(270)
        che.forward(100)

    if che.xcor() < -280:
        che.setheading(0)
        che.forward(100)

    if che.ycor() < -280:
        che.setheading(90)
        che.forward(100)
    
    che.forward(random_move)
    che.left(random_turn)

    



wn.exitonclick()