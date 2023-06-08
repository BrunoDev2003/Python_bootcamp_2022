from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()

screen.setup(width=800, height=800)
screen.bgcolor("green")
screen.title("SNAAAAAKEEEEE")


snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()






screen.exitonclick()