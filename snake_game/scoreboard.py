from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 280)
        self.score = 0
        self.color("White")
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=("Arial", 8, "normal"))

    def refresh_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=("Arial", 8, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", move=False, align="center", font=("Arial", 16, "normal"))

