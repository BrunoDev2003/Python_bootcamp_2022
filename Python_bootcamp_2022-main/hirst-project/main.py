import colorgram 
import turtle as t 
import random

bruno = t.Turtle()
rgb_colors = []
bruno.speed("fastest")
colors = colorgram.extract('image.jpg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

bruno.setheading(225)
bruno.forward(300)
bruno.setheading(0)

for dot in range(1, number_of_dots):
    bruno.dot(20, random.choice(color_list))
    bruno.forward(50)
    bruno.position()
    bruno.heading()

    if dot & 10 == 0:
        bruno.forward(50)
        bruno.position()
        bruno.heading()

bruno.setheading(90)
bruno.foward(50)
bruno.setheading(180)
bruno.foward(500)
bruno.setheading(0)

screen = t.Screen()
screen.exitonclick()

