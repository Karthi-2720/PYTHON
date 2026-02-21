from turtle import Turtle

FONT = ("Courier", 24, "bold")
INCREASE_LEVEL = 0

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()

    def game_over(self):
        self.color("black")
        self.penup()
        self.write("GAME OVER", align="center", font=FONT)
        self.goto(0, 0)

    def level(self):
        self.color("black")
        self.penup()
        self.goto(-200, 250)
        self.write(f"LEVEL UP:{INCREASE_LEVEL}", align="center", font=FONT)

    def increase_level(self):
        global INCREASE_LEVEL
        self.clear()
        INCREASE_LEVEL += 1