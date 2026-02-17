import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

directions = [0, 90, 180, 270]
d = True
f = 0

tim.pensize(15)
tim.speed("fastest")

def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

while d:
    tim.color(color())
    tim.setheading(random.choice(directions))
    tim.forward(30)
    f += 1
    if f == 500:
        d = False

t.done()
