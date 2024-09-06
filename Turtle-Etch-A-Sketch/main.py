from turtle import Turtle, Screen

scrn = Screen()

che = Turtle()
che.shape("turtle")

def go_up():
    che.setheading(90)
    che.forward(50)

def go_down():
    che.setheading(270)
    che.forward(50)

def go_right():
    che.setheading(0)
    che.forward(50)

def go_left():
    che.setheading(180)
    che.forward(50)

def pen_up():
    che.penup()

def pen_down():
    che.pendown()

scrn.listen()

scrn.onkey(go_up, "Up")
scrn.onkey(go_down, "Down")
scrn.onkey(go_left, "Left")
scrn.onkey(go_right, "Right")
scrn.onkeypress(pen_up, "w")
scrn.onkeyrelease(pen_down, "w")

scrn.exitonclick()