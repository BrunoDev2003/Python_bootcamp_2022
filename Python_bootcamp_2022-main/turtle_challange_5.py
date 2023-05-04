import turtle as t 
import random

bruno = t.Turtle()

def randomColor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color



bruno.speed("fastest")

def draw_spirograph(size_of_gap):
    for __ in range(int(360/size_of_gap)):
        bruno.color(randomColor())
        bruno.circle(100)
        bruno.set_heading(bruno.heading() + size_of_gap)

draw_spirograph(3)

screen = t.Screen()
screen.exitonclick()