from turtle import Turtle, Screen
import random

wn = Screen()
wn.setup(600, 600)

che = Turtle()
che.shape("turtle")

while(True):

    random_move = random.randint(5, 50)
    random_turn = random.randint(0, 360)

    if (che.xcor() > 280 or che.ycor() > 280 or che.xcor() < -280 or che.ycor() < -280):
        che.backward(100)

    
    che.forward(random_move)
    che.left(random_turn)

    



wn.exitonclick()