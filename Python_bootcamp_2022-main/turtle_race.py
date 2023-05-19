from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

for turtle in range(0, 6):
    bruno = Turtle(shape="turtle")
    bruno.color(colors[turtle])
    bruno.penup()
    bruno.goto(x=-230, y=y_positions[turtle])



screen.exitonclick()