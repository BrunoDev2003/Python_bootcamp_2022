
starting_positions = [(0,0), (-20, 0), (-40,0)]
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

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
            screen.update()
            time.sleep(1)

            for seg_num in range(len(segments) - 1,0,-1):
                new_x = self.segments[seg_num - 1].xcor()
                new_y = self.segments[seg_num - 1].ycor()
                self.segments[seg_num].goto(new_x, new_y)
            self.segments[0].forward(20)
            self.segments[0].left(90)
