from turtle import Screen, Turtle

screen = Screen()

screen.setup(width=800, height=800)
screen.bgcolor("green")
screen.title("SNAAAAAKEEEEE")

t1 = Turtle("Square")
t2 = Turtle("Square")
t3 = Turtle("Square")

t1.color("white")
t2.color("white")
t3.color("white")

t1.goto(-20, 0)
t2.goto(-40,0)
t3.goto(-60,0)

t1.pensize(20)
t2.pensize(20)
t3.pensize(20)



screen.exitonclick()