from turtle import Turtle, Screen
import random
import colorgram
screen = Screen()
screen.colormode(255)
tim = Turtle()
tim.hideturtle()
# colors = colorgram.extract('image.jpg', 30)
# color_rgb = []
# for color in colors:
#   RGB = (color.rgb.r, color.rgb.g, color.rgb.b)
#   color_rgb.append(RGB)
#
# print(color_rgb)
colors = [(201, 151, 106), (128, 101, 51), (183, 153, 24), (48, 48, 9), (82, 86, 11), (15, 42, 7), (249, 224, 166),
          (81, 92, 102), (102, 85, 91), (242, 201, 116), (136, 160, 150), (79, 114, 77), (164, 114, 99), (43, 87, 20),
          (40, 47, 58), (57, 62, 74), (103, 143, 124)]
tim.penup()
tim.goto(-200, -200)
d = True
tim.speed(0)
x1 = -200
y1 = -200
y = 0
def hi():
    global d, y
    y += 1
    if y == 10:
        d = False
    if d:
        return print_dot()
    return None
def print_dot():
    global d,y1,x1
    x = 0
    while d:
        tim.dot(20, random.choice(colors))
        tim.forward(50)
        x += 1
        if x == 10:
            y1=y1+50
            tim.goto(x1,y1)
            return hi()
    return None

print_dot()

screen = Screen()
screen.exitonclick()
