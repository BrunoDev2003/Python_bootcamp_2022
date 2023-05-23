from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
all_turtles = []
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

for turtle in range(0, 6): 
    bruno = Turtle(shape="turtle")
    bruno.color(colors[turtle])
    bruno.penup()
    bruno.goto(x=-230, y=y_positions[turtle])

if user_bet:
    is_race_on: True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner of the race!")
            else:
                print(f"You've lost! The {winning_color} turtle is the loser of the race!")
        rand_distance = random.randint(0, 10)
        turtle.foward(rand_distance)



screen.exitonclick()