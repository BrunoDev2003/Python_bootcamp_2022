from turtle import Turtle,Screen


bruno = Turtle()
screen = Screen()

def move_forward():
    bruno.forward(10)

def move_backwards():
    bruno.backward(10)
def turn_right():
    bruno.right(10)

def turn_left():
    bruno.left(10)

def clear():
    bruno.clear()
    bruno.home()
    bruno.clear()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()