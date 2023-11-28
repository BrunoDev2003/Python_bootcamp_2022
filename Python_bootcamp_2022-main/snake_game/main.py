from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()

snake = Snake()

screen.setup(width=800, height=800)
screen.bgcolor("green")
screen.title("SNAAAAAKEEEEE")
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()






screen.exitonclick()