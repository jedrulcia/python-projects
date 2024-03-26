from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-50, 200)
        self.write(self.l_score, align="center", font=("Arial", 60, "normal"))
        self.goto(0, 200)
        self.write(":", align="center", font=("Arial", 60, "normal"))
        self.goto(50, 200)
        self.write(self.r_score, align="center", font=("Arial", 60, "normal"))

    def display_winner(self, side):
        self.clear()
        self.goto(0, 0)
        self.write(f"Player on the {side} has won!", align="center", font=("Arial", 40, "normal"))