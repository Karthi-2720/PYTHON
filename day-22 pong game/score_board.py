from turtle import Turtle



class Scoreboard(Turtle):
    def __init__(self, position_score):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('black')
        self.goto(position_score)


    def l_score(self, num):
        self.clear()
        self.write(f"{num}", align="center", font=("Courier", 50, "bold"))

    def r_score(self, num):
        self.clear()
        self.write(f"{num}", align="center", font=("Courier", 50, "bold"))