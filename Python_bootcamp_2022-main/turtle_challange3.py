import turtle as t

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########

def draw_shapes(num_sides):
    angles = 360/num_sides
    for __ in range(num_sides):
        tim.forward(100)
        tim.right(angles)

for shape_side in range(3,11):
    draw_shapes(shape_side)

