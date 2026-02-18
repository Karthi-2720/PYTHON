from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()
screen.listen()
def move():
    tim.forward(10)
def back():
    tim.backward(10)
def left():
    tim.left(10)
def right():
    tim.right(10)
def reset():
    tim.reset()

screen.onkeypress(key="w", fun=move)
screen.onkeypress(key="s", fun=back)
screen.onkeypress(key="a", fun=left)
screen.onkeypress(key="d", fun=right)
screen.onkeypress(key="c", fun=reset)
screen.exitonclick()