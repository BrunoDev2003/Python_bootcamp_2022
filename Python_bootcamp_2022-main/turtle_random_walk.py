import turtle as t 
import random

bruno = t.Turtle()

colours = ["IndianRed","CornFlowerBlue","DeepSkyBlue"]
directions = [0, 90, 100, 200]
bruno.pensize(15)
bruno.speed(100)

for __ in range(10):
    bruno.color(random.choice(colours))
    bruno.forward(30)
    bruno.setheading(random.choice(directions))

input("click something")