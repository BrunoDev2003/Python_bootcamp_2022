import turtle as t 
import random 

bruno = t.Turtle()
t.colormode(255)

def randomColor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

directions = [0,90,180,270]
bruno.pensize(15)
bruno.speed("fastest")


for __ in range(200):
    bruno.color(random_color())
    bruno.forward(30)
    bruno.setheading(random.choice(directions))