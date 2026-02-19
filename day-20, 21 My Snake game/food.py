from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("green")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh()

    def refresh(self) :
        x_food = random.randint(-280, 280)
        y_food = random.randint(-280, 250)
        self.goto(x_food, y_food)

