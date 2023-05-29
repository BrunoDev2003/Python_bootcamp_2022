from turtle import Screen, Turtle

screen = Screen()

screen.setup(width=800, height=800)
screen.bgcolor("green")
screen.title("SNAAAAAKEEEEE")


segments = []


starting_positions = [(0,0),(-20,0),(-40,0)]


for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)

game_on = True
while game_on:
    for seg in segments:
        seg.foward(20)


screen.exitonclick()