
from turtle import _Screen, Turtle
import time


starting_positions = [(0,0), (-20, 0), (-40,0)]
MOVE_DISTANCE = 20
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

def create_snake(self):
        for position in starting_positions:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)

game_on = True
def move(self):

    while game_on:
        for self.seg in self.segments:
            _Screen.update()
            time.sleep(1)

            for seg_num in range(len(self.segments) - 1,0,-1):
                new_x = self.segments[seg_num - 1].xcor()
                new_y = self.segments[seg_num - 1].ycor()
                self.segments[seg_num].goto(new_x, new_y)
            self.head.forward(MOVE_DISTANCE)
            self.head.left(90)

def up(self):
        
        self.head.setheading(90)

def down(self):
    self.head.setheading(270)

def left(self):
    self.head.setheading(180)

def right(self):
    self.head.setheading(0)