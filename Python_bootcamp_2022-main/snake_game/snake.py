
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)

game_on = True
while game_on:
    for seg in segments:
        screen.update()
        time.sleep(1)

        for seg_num in range(len(segments) - 1,0,-1):
            new_x = segments[seg_num - 1].xcor()
            new_y = segments[seg_num - 1].ycor()
            segments[seg_num].goto(new_x, new_y)
        segments[0].forward(20)
        segments[0].left(90)