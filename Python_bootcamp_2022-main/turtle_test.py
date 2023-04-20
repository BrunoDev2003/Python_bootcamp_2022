from turtle import Turtle, Screen


bruno_turtle = Turtle()


for _ in range(15):
    bruno_turtle.forward(10)
    bruno_turtle.penup()
    bruno_turtle.forward(15)
    bruno_turtle.pendown()
input("Press any key to exit ...")
