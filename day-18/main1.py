import turtle as t
import random
tim = t.Turtle
g = 0
t.speed(0)
t.colormode(255)

def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def karthikeya(size_of):
    for i in range(int(360 / size_of)):
        t.color(color())
        t.left(size_of)
        t.circle(100)

karthikeya(10)