from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(-265, 280)
        self.score = 0
        self.color("White")
        self.write(arg=f"Round: {self.score}", move=False, align="center", font=("Arial", 12, "normal"))

    def refresh_score(self):
        self.clear()
        self.write(arg=f"Round: {self.score}", move=False, align="center", font=("Arial", 12, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", move=False, align="center", font=("Arial", 16, "normal"))
        self.goto(0, -30)
        self.write(arg=f"Your score: {self.score}", move=False, align="center", font=("Arial", 12, "normal"))