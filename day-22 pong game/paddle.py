from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.left(90)
        self.penup()
        self.setposition(position)
        self.color('black')
        self.shapesize(stretch_wid=1, stretch_len=5)


    def up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)

    def up_l(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def down_l(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)

