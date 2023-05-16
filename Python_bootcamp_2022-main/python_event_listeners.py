from turtle import Turtle,Screen


bruno = Turtle()
screen = Screen()

def move_forward():
    bruno.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()