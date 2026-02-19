from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        with open("high_score.txt", "r") as f:
            self.highest_score = int(f.read())
        self.goto(0, 270)
        self.hideturtle()
        self. update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score}     Highest Score: {self.highest_score} ", align="center",
                   font=("Arial", 20, "normal"))

    def reset_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
        self.score = 0
        with open("high_score.txt", "w") as file:
            file.write(str(self.highest_score))


        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()