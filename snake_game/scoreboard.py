from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 280)
        self.score = 0
        file = open("highest_score.txt")
        self.highest_score = int(file.read())
        file.close()
        self.color("White")
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} Highest Score: {self.highest_score}", move=False, align="center", font=("Arial", 8, "normal"))

    def reset(self):
        if (self.score > self.highest_score):
            self.highest_score = self.score
            file = open("highest_score.txt", mode="w")
            file.write(str(self.highest_score))
            file.close()
        self.score = 0
        self.refresh_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", move=False, align="center", font=("Arial", 16, "normal"))

