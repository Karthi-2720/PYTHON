import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="bet the race", prompt="Chose the one of the turtle. Let's begin the race.")
y = [-150, -100, -50, 0, 50, 100, 150]
tim_color = ["red", "orange", "blue", "green", "yellow", "pink", "purple"]
all_turtles = []
is_on = True

for turtle_index in range(0, 7):
    new_tim = Turtle(shape="turtle")
    new_tim.penup()
    new_tim.goto(-230, y[turtle_index])
    new_tim.color(tim_color[turtle_index])
    all_turtles.append(new_tim)

if user_bet:
    is_on = True

while is_on:

    for turtle in all_turtles:
        random_speed = random.randint(0, 10)
        turtle.forward(random_speed)
        if turtle.xcor() > 230:
            is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"{user_bet} win")
            else:
                print(f"{user_bet} loose and winning is {winning_color}")
screen.exitonclick()